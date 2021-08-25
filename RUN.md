# To run MapReduce

1.  Install Java and Eclipse
2.  Download the MapReduce zip file
3.  Open MapReduce folder dir in eclipse
4.  Select Run as > Run Configuration
5.  Open environment tab, add below paths & check 'Append env to native env',&apply 
    HADOOP_HOME with value C:\Users\YourUsername\eclipse-workspace\MapReduce\hadoop-libs\win32
    PATh with value C:\Users\YourUsername\eclipse-workspace\MapReduce\hadoop-libs\win32\bin
6.  Open Argument tab, add INPUT.txt output (input text file and an output folder for output)
7.  Open the wordcount java file in src/bigdatax.mapreduce.wordcount
8.  Run the wordcount java file, press Run as > Java Application
9.  The output can be found in output folder (from part 6), file name part-r-0000
10. To write another mapreduce program, Start by making a copy of the wordcount package from above, by right-clicking on the package bigdatax.mapreduce.wordcount, selecting Copy, then right-clicking on the src folder and choosing Paste.
11. Choose a new name for the package, then click OK.
12. Don't forget to add a new Run Configuration for each package you create with the specific parameters required.

for wordcount2 arguments -> FirstInputFile.txt SecondInputFile.txt output2 outputfinal

# NEXT TASK TODOOOO
Page Rank with map reduce

1. in mapreduce.pagerank package
2. data is already sorted out in node1 - related nodes to the node1
3. next step is to create another mapreduce job to do page rank
4. problem is i dont know how to do it and i am confused
5. lets move on to another concepts first and come back here again
