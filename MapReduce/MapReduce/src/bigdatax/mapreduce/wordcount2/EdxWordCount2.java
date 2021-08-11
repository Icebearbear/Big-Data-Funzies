package bigdatax.mapreduce.wordcount2;
//import multipleInput.Join;

import java.io.IOException;
import java.util.StringTokenizer;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

import bigdatax.mapreduce.wordcount.EdxWordCount;
import bigdatax.mapreduce.wordcount.EdxWordCount.EdxCombiner;
import bigdatax.mapreduce.wordcount.EdxWordCount.EdxMap;
import bigdatax.mapreduce.wordcount.EdxWordCount.EdxReduce;

import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.MultipleInputs;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.fs.Path;

public class EdxWordCount2
{	
	public static class File1Mapper extends Mapper<LongWritable,Text,Text,IntWritable> {
		private Text word = new Text();
		public void map(LongWritable key, Text value,Context context) throws IOException,InterruptedException{
			
			String line = value.toString().toLowerCase();
			StringTokenizer tokenizer = new StringTokenizer(line); // splits the lines into tokens separated by whitespaces via StringTokenizer
			while (tokenizer.hasMoreTokens()) {	// if there are more words in tokenizer, 
				word.set(tokenizer.nextToken());	// keep creating next token until there are no more token in tokenizer
				context.write(word ,new IntWritable(1));	// it creates this format <word, 1>
			}
		}
	}
	public static class File2Mapper extends Mapper<LongWritable,Text,Text,IntWritable> {
		private Text word = new Text();
		public void map(LongWritable key, Text value,Context context) throws IOException,InterruptedException{
			
			String line = value.toString().toLowerCase();
			StringTokenizer tokenizer = new StringTokenizer(line); // splits the lines into tokens separated by whitespaces via StringTokenizer
			while (tokenizer.hasMoreTokens()) {	// if there are more words in tokenizer, 
				word.set(tokenizer.nextToken());	// keep creating next token until there are no more token in tokenizer
				context.write(word, new IntWritable(1));	// it creates this format <word, 1>
			}
		}
	}
	public static class FileMapper2 extends Mapper<LongWritable,Text,Text,IntWritable> {
		private Text word = new Text();
		public void map(LongWritable key, Text value,Context context) throws IOException,InterruptedException{
			
			String line = value.toString().toLowerCase();
			StringTokenizer tokenizer = new StringTokenizer(line); // splits the lines into tokens separated by whitespaces via StringTokenizer
			while (tokenizer.hasMoreTokens()) {	// if there are more words in tokenizer, 
				String str = Integer.toString(tokenizer.nextToken().length());
				word.set(str);	// keep creating next token until there are no more token in tokenizer
				context.write(word ,new IntWritable(1));	// it creates this format <word, 1>
			}
		}
	}
	
	public static class EdxCombiner1 extends Reducer<Text,IntWritable,Text,IntWritable> {
		public void reduce(Text key, Iterable<IntWritable> values,Context context) throws IOException,InterruptedException {
			int sum=0;
			for(IntWritable x: values)
			{
				sum+=x.get();
				// only write once for repeated words
				if (sum == 1)
					context.write(key, new IntWritable(sum));
			}
		}
	}
	
	public static class EdxCombiner2 extends Reducer<Text,IntWritable,Text,IntWritable> {
		public void reduce(Text key, Iterable<IntWritable> values,Context context) throws IOException,InterruptedException {
			int sum=0;
			for(IntWritable x: values)
			{
				sum+=x.get();
			}
			context.write(key, new IntWritable(sum));
		}
	}

	public static class EdxReduce1 extends Reducer<Text,IntWritable,Text,IntWritable> {
		public void reduce(Text key, Iterable<IntWritable> values,Context context) throws IOException,InterruptedException {
			int sum=0;
			for(IntWritable x: values)
			{
				sum+=x.get();
				// only write once for repeated words
				if (sum == 1)
					context.write(key, new IntWritable(sum));
			}
		}
	}
	
	public static class EdxReduce2 extends Reducer<Text,IntWritable,Text,IntWritable> {
		public void reduce(Text key, Iterable<IntWritable> values,Context context) throws IOException,InterruptedException {
			int sum=0;
			for(IntWritable x: values)
			{
				sum+=x.get();
			}
			context.write(key, new IntWritable(sum));
		}
	}
	
	
	public static void main(String[] args) throws Exception {
		
//		FIRST JOB IS TO REMOVE THE DUPLICATES OF WORDS. WORD COUND OF NON DUPLICATED WORDS
		Configuration conf1 = new Configuration();
		Job job = new Job(conf1, "Test");
		job.setJarByClass(EdxWordCount2.class);
		
		// creating 2 paths for 2 different inputs - add one more inputs in Arguments tab
		// creating 1 path for output
		MultipleInputs.addInputPath(job, new Path(args[0]), TextInputFormat.class, File1Mapper.class);
		MultipleInputs.addInputPath(job, new Path(args[1]), TextInputFormat.class, File2Mapper.class);
		FileOutputFormat.setOutputPath(job, new Path(args[2]));
		
		job.setCombinerClass(EdxCombiner1.class);
		job.setReducerClass(EdxReduce1.class);
		job.setNumReduceTasks(1);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);

		job.waitForCompletion(true);
//		System.exit(0);
		
//		SECOND JOB IS TO COUNT THE NUMBER OF LETTERS AND COUNT EACH WORD 
//		IF NEED TO CHAIN MAPREDUCE, CREATE ANOTHER JOB. OUTPUT OF FIRST JOB IS INPUT FOR SECOND JOB
		Job job2 = Job.getInstance();
		job2.setJarByClass(EdxWordCount2.class);
		job2.setJobName("Edxmapreduce");
		
		job2.setMapperClass(FileMapper2.class);
		job2.setCombinerClass(EdxCombiner2.class);
		job2.setReducerClass(EdxReduce2.class);
		
		job2.setOutputKeyClass(Text.class);
		job2.setOutputValueClass(IntWritable.class);
		
		job2.setInputFormatClass(TextInputFormat.class);
		job2.setOutputFormatClass(TextOutputFormat.class);

		FileInputFormat.addInputPath(job2, new Path(args[2]));
		FileOutputFormat.setOutputPath(job2, new Path(args[3]));
		
		job2.waitForCompletion(true);
		System.exit(0);
	}

}