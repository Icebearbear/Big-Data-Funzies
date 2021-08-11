package bigdatax.mapreduce.wordcount;

import java.io.IOException;
import java.util.StringTokenizer;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.fs.Path;

public class EdxWordCount
{	
	public static class EdxMap extends Mapper<LongWritable,Text,Text,IntWritable> {
		private Text word = new Text();
		public void map(LongWritable key, Text value,Context context) throws IOException,InterruptedException{
			
			String line = value.toString().toLowerCase();
			StringTokenizer tokenizer = new StringTokenizer(line); // splits the lines into tokens separated by whitespaces via StringTokenizer
			while (tokenizer.hasMoreTokens()) {	// if there are more words in tokenizer, 
				String str = Integer.toString(tokenizer.nextToken().length());
				word.set(str);	// keep creating next token until there are no more token in tokenizer
				context.write(word, new IntWritable(1));	// it creates this format <word, 1>
			}
		}
	}
	
	public static class EdxCombiner extends Reducer<Text,IntWritable,Text,IntWritable> {
		public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException
	    {
			int sum=0;
			for (IntWritable x: values)
			{
				sum+=x.get();
			}
			context.write(key, new IntWritable(sum));
		}
	}

	public static class EdxReduce extends Reducer<Text,IntWritable,Text,IntWritable> {
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
		
		Job job = Job.getInstance();
		job.setJarByClass(EdxWordCount.class);
		job.setJobName("Edxmapreduce");
		
		job.setMapperClass(EdxMap.class);
		job.setCombinerClass(EdxCombiner.class);
		job.setReducerClass(EdxReduce.class);
		
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);
		
		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);

		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));
		
		job.waitForCompletion(true);
		System.exit(0);
	}

}