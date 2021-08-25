package bigdatax.mapreduce.pagerank;

import java.io.IOException;
import java.util.ArrayList;
import java.util.StringTokenizer;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.mortbay.log.Log;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.fs.Path;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class PageRank
{
		
		public static class Map extends Mapper<LongWritable,Text,IntWritable,IntWritable> {
			private static final transient Logger LOG = LoggerFactory.getLogger(PageRank.class);
			int len = 0;
			ArrayList<Integer> list = new ArrayList<Integer>(len);
			public void map(LongWritable key, Text value,Context context) throws IOException,InterruptedException{
				String line = value.toString();
				String[] nodes = line.split("\t");
				len = nodes.length-1;
				context.write(new IntWritable(Integer.parseInt(nodes[0])), new IntWritable(Integer.parseInt(nodes[1])));
			}
		}
		
//		public static class Map2 extends Mapper<IntWritable,Text,IntWritable,Text> {
//			private static final transient Logger LOG = LoggerFactory.getLogger(PageRank.class);
//			int len = 0;
//			ArrayList<Integer> list = new ArrayList<Integer>(len);
//			public void map(IntWritable key, Text value,Context context) throws IOException,InterruptedException{
//				String line = value.toString();
//				String[] nodes = line.split(",");
////				double p = pageRank / nodes.length;
//				context.write(key, value);
//				
//				context.write(new IntWritable(Integer.parseInt(nodes[0])), new IntWritable(Integer.parseInt(nodes[1])));
//			}
//		}
	

	public static class Reduce extends Reducer<IntWritable,IntWritable,IntWritable,Text> {
		private static final transient Logger LOG = LoggerFactory.getLogger(PageRank.class);
		public void reduce(IntWritable key, Iterable<IntWritable> values,Context context) throws IOException,InterruptedException {
			int sum=0;
			String data = "";
			ArrayList<Integer> list = new ArrayList<Integer>();
			for(IntWritable x: values)
			{
				if (sum == 0) {
					list.clear();
					data += x.get();
				}
//				list.add(x.get());
				else {
					data += "," + x.get();
				}
				
				sum+=x.get();
			}
			context.write(key, new Text(data));
			
		}
	}
	
	public static class Reduce2 extends Reducer<IntWritable,IntWritable,IntWritable,Text> {
		private static final transient Logger LOG = LoggerFactory.getLogger(PageRank.class);
		public void reduce(IntWritable key, Iterable<IntWritable> values,Context context) throws IOException,InterruptedException {
			int sum=0;
			ArrayList<Integer> list = new ArrayList<Integer>();
			for(IntWritable x: values)
			{
				if (sum == 0) {
					list.clear();
				}
				list.add(x.get());
				sum+=x.get();
			}
			context.write(key, new Text(list.toString()));
		}
	}
	
	public static void main(String[] args) throws Exception {
		
		Job job = Job.getInstance();
		job.setJarByClass(PageRank.class);
		job.setJobName("pagerank mapreduce");
		
		job.setMapperClass(Map.class);
		job.setReducerClass(Reduce.class);
		
		job.setOutputKeyClass(IntWritable.class);
		job.setOutputValueClass(Text.class);
		job.setMapOutputKeyClass(IntWritable.class);
		job.setMapOutputValueClass(IntWritable.class);
		
		job.setInputFormatClass(TextInputFormat.class);
		job.setOutputFormatClass(TextOutputFormat.class);

		FileInputFormat.addInputPath(job, new Path(args[0]));
		FileOutputFormat.setOutputPath(job, new Path(args[1]));
		
		job.waitForCompletion(true);
		System.exit(0);
		
//		Job job2 = Job.getInstance();
//		job2.setJarByClass(PageRank.class);
//		job2.setJobName("pagerank mapreduce2");
//		
//		job2.setMapperClass(Map2.class);
//		job2.setReducerClass(Reduce2.class);
//		
//		job2.setOutputKeyClass(IntWritable.class);
//		job2.setOutputValueClass(Text.class);
//		job2.setMapOutputKeyClass(IntWritable.class);
//		job2.setMapOutputValueClass(IntWritable.class);
//		
//		job2.setInputFormatClass(TextInputFormat.class);
//		job2.setOutputFormatClass(TextOutputFormat.class);
//
//		FileInputFormat.addInputPath(job2, new Path(args[1]));
//		FileOutputFormat.setOutputPath(job2, new Path(args[2]));
//		
//		job2.waitForCompletion(true);
//		System.exit(0);
	}

}