# To run MapReduce

1.  Install Java and Eclipse
2.  Download the MapReduce zip file
3.  Open MapReduce folder dir in eclipse
4.  Select Run as > Run Configuration
5.  Open environment tab, add below paths & check 'Append env to native env',&apply 
    HADOOP_HOME with value C:\Users\YourUsername\eclipse-workspace\MapReduce\hadoop-libs\win32
    PATh with value C:\Users\YourUsername\eclipse-workspace\MapReduce\hadoop-libs\win32\lib
6.  Open Argument tab, add INPUT.txt output (input text file and an output folder for output)
7.  Open the wordcount java file in src/bigdatax.mapreduce.wordcount
8.  Run the wordcount java file, press Run as > Java Application
9.  The output can be found in output folder (from part 6), file name part-r-0000
10. To write another mapreduce program, Start by making a copy of the wordcount package from above, by right-clicking on the package bigdatax.mapreduce.wordcount, selecting Copy, then right-clicking on the src folder and choosing Paste.
11. Choose a new name for the package, then click OK.
12. Don't forget to add a new Run Configuration for each package you create with the specific parameters required.