# Big-Data-Funzies

## Section 1
### Four V 
is the key of understanding the challenges in big data. four V :
1.  Volume - large amount of data
2.  Velocity - the speed at which the data arrives. Due to the hight velocity of data, it is not feasible to store and check all data. Hence, we look at sampling techniques that store a representatice fraction of the data
3.  Veracity - uncertainty that comes with data. data is not complete and requires data cleaning to reduce the veracity.e.g missing location,
4.  Variety - different sources of big data. data comes with different forms, pictures, string, videos, etc. you have to integrate data fromvarious sources 

### Bonferroni's principle 
The expected number of events found by a method in random big data is significantly higher than the number of events you expected. The key observation is that even if the data is random, then with enough data, you will still observe a large number of rare events. 
Assume that you have a facial recognition camera system that is 99.9% reliable. Assume that the airport uses the system to detect known criminals by comparing selected facial features from each person to a face database of known criminals. If a person is a known criminal, then the probability that they are not detected is 0.01% - a false negative. If a person is not a criminal, then he or she is flagged as a criminal with probability 0.01% - a false positive. Assume one in 10 million people coming through the system are known criminals. This would mean that 1,000 people who aren't criminals are flagged as criminals by the system. So there are many false alarms, and a security guard, using the system, would get roughly 1,000 false alarms before a real criminal gets flagged. Security might think that the real criminal is just another false alarm and ignore it.

### Probability
probability of getting head of a coin toss with k number of times experiments will be 1- (1- p/k)^k = 1-exp(p) assuming k is large enough. 
e.g p is probability of getting a head in a single coin toss is 0.5 and having 10 heads in a row is p = 0.5^10 = 0.000097. for the k numbers of experiments of the head tossing coins, the probability will be 1- e(-1/1024) = 0.000097

### Data Mining
is a process of finding models(patterns and correlation) within a large set of data to predict outcomes. 

One example is PageRank by Google. it models the importance of web pages in the internet. Pages are connected through links. each pages is assigned a value to summarize the importance of that page which is the probability that the surfer is at this page at any given point of time. Page rank of a page is high if it is regarded as important by other pages that link to it. By having the web pages modelled this way, it allows algo to judge the importance of pages as part of an internet search engine.

### Data Modelling
Modelling data allows for concise summary for a large and complex data sets.
Imaging ff there exist 1 billion website and each website took 1 milisec to load. how long does the search engine take to go through all the existing websites everytime a user makes a search query? it will take 11 days! If you can summarise all websites in a concise manner, it allows searches to be performed much more efficiently.

#### Methods of data modelling:
1.  Gaussian Distribution
2.  Clustering
3.  Power law degree distribution

## Section 2 Web and Social Networks
from previous section, we learnt that if you want to analyse data, we have to obtain models from our data for data mining algorithms. But before that, we should find a good way to model (data modelling) the data and we should look into their characteristics first. 

e.g in social networks, there exist many models. We have users as entities and relationship between them which is referred to as "friends". For example of small social network, say we use nodes to denote entities and model the social network as a graph. The nodes are connected by and edge with the nodes are related by the relationship that characterises the social network- frienships. there are many more social networks and there can be many types of entities in a graph

one example, in a network there are 3 entities, users, tags, videos. If the users tend to use the same tags frequently or if they tend to tag the same videos, then we would expect them to be connected in the network. Similarly, tags can be regarded as relevant if they are often given to the same videos or are used by the same users. The videos can be considered similar if they have many similar tags.
A better way to represent these pieces of information is through the use of K-partite graphs for some K >1. In general, a K-partite graph consists of  disjoint sets of nodes, with no edges between nodes of the same set.

Social network have defining characteristics and have focused on 
#### Three distinctive features relating to a social network structure :
1.  Small-world Effect - through the experiment of posting letters from one person to another through non-acquaintances, Stanley Milgram discovered that distant people are reachable through a very short chain with a length of chain of six which is the foundation of Six Degrees of Separation
2.  Clustering - probability of two of your friends know each other is much greater that two people randomly from facebook to know each other
3.  Having a skewed degree - in graph theory, the degree of node = number of edges that connects to it. degree distribution = probability distribution of these degrees in the graph

Modelling the relationship between entities in social network is crucial for data mining algorithm. From modelling perspective, a network is just a sets of nodes with links between them. The real challange is to decide on how to put the edges between them so that the graph can well represent the complexity of the social network
#### The common ways to model a social network :
1.  Random graphs
    exist n nodes with edges with probability p. the degrees of graph follow a Poisson Distribution, a discrete probability distribution that experesses probability of a certain number of events that happen in a fixed interval of time, space, or volume.
    The number of events is a random variable, which may or may not follow the Poisson Distribution. If the following requirements are fulfilled, you can expect the value of the events actually follows the Poisson Distribution.
    a. events are happening independently.
    b. the probability that a certain event occurs in a fixed interval of time stays the same through time.

    With this definition, the links in a random graph are added independently and randomly. Although the real networks are not Poisson, the random networks provide us a useful model to do some initial analysis.
2.  Scale free graph
    it is a network where there are a significant number of highly connected nodes. the degree distribution of the nodes follow [a power law](https://www.statisticshowto.com/power-law/).

    With scale free graph, for example in wiki, article = entities, references links to another article = edges. With more references the links = more edges = higher degree of node (proportional to K). this kind of network is robust to network failures because after some random vertices got deleted, the networks is still connected (?)
3.  Small world graph
    A small world graph has a high clustering coefficient which reflects the properties of this kind of graph where the nodes tend to form cliques. It can be used as a measure of the tendency of nodes to cluster together. the higher the probability p(0,1), the higher the randomness of the graph.

graph can be represented as matrix

[Activity 1: Modelling a small social network & Quiz 3](https://docs.google.com/spreadsheets/d/18NGLsWuAlNifVYzabaOiGNqrCHNzGV8OwmR7wtw1rHw/edit?usp=sharing/)

### [Community detection in social network](https://www.analyticsvidhya.com/blog/2020/04/community-detection-graphs-networks/)
Social network contains communities of entities(users) that are connected with relationship (edges)
we can FIND COMMUNITIES using a measure called betweenness and an algorithm that relies on edge removal

#### Calculating betweenness in a graph
betweenness is used to measure the centrality of a graph based in the shortest path in it. There can be more than one shortest path. it is to search for communities by partitioning all individuals 
##### Betweenness:
1.  Node betweenness
    find in the picture Betweeness of Nodes.png
2.  Edge Betweenness
    The edge betweenness centrality is defined as the number of the shortest paths that go through an edge in a graph or network
    find in picture Betwenness of edges of nodes.png
3.  Complexity 
    find in picture Complexity.png

#### Finding communities using betweenness
##### Edge Removal:
to get a individuals in multiple communities, after calculating edges betweenness, we use edge removal to remove edges from the highest betweenness and recalculate the edge betweenness and repeat. The result will give us the communities 

##### Gravin-Newman Algorithm
1.  find the shortest path between nodes
2.  find the edge betweenness
3.  the edge with highest betweenness are removed
4.  the betweenness of all edges affected by the edge removal are recalculated '
5.  steps 3 and 4 are repeated until no edges remain

### Clustering Methods
#### MCL (picture at MCL.png)
modelling the flow in the graph. it is also can be described as a random walk through a graph. 
1.  Use adjacency matrix to show the connections between nodes. One of the benefits to present the graph in a adjacency matrix is that you can easily find the number of paths with different sizes between nodes.
e.g an adjacency matrix M, it represents the path with length 1 between nodes. To find path with length 2, simply find M*M (M^2)
2. The point is to distinguish paths within the same cluster. Create self-loop by calculating M + I (identity matrix) 
3. Find transision matrix.  The main point is to show that the nodes are within one cluster or not with number, e.g within cluster is 1.5 and not within cluster is 0. In plain English you want to divide each element in a column by the sum of the column. Do that for all the elements. In matrix M, The value of each elements Tij represent the amount that the flow/random walker is attracted to node i to j with 1 step. Same idea if you multiple the matrix M by itself, you are increasing the number of step between nodes. 
4. but you cant keep multiplying bcs you wont see the cluster. you have to Normalise the Transisition matrix. Define a value r. This is similar to how you normalised the transition matrix on the previous page. For each element in each column, the new value (Tij) equals that element raised to the power of (r) divided by the sum of the elements in the column, each raised to the power of (r) (you sum each element to the power of r, not calculate the sum and raise that to the power of (r)). It makes the big number bigger and small number smaller.
5. each matrix row of non zero will be the cluster

### Hierarchical clustering, 
it covers these key concepts:

Essential questions: 
1. How should a cluster be presented? 
2. How should I choose two clusters to merge?  
3. When should merging stop?

If you can answer the above question then you can use hierarchical clustering
Steps of the algorithm:
1. Choose the two nearest clusters.
2. Merge the chosen clusters.
3. Repeat Step 1 and Step 2 until the stopping criteria has been met.

How it works:
1.  it will find the centroid between 2 nodes, the average location between the 2 nodes is the centroid location
2.  you can slowly create cluster by using the centroid from step 1 to another node and get another centroid between them
3.  you can continue based on your application/objective

How to control, the alternative approach:
1. Defining the distance of two clusters as the minimum distance between pairs, where each element is from a different cluster. it is by using averange distance between all possible pairs of points
2.  Merging two clusters on the condition that the new cluster is the one with the smallest radius. The radius of a cluster is the maximum distance between the centroid and the points of that cluster.
3.  Using the diameter of a cluster as the factor and merge clusters which result in the smallest diameter. The diameter of a cluster is the maximum distance of all pairs of points in that cluster.

When should we stop the clustering. different approach that we can take:
1.  The algorithm stops when the density of the best merged clusters become less than some threshold.
The density can be defined according to different factors like diameter or radius. For example, in a two-dimensional space, you may compute the density of a cluster by dividing the number of its nodes by the square of its radius to demonstrate the number of points of the cluster in its unit volume. Unit could also be defined as the radius to the power of dimension. So, if the best merge causes a new cluster with small density, the merged clusters were pretty far from each other.
2.  The algorithm stops if the diameter of the next best merging cluster exceeds some limit.
The factor could be radius or any variant related to it.
3.  The algorithm stops if a combination of clusters generates a bad cluster.
For example, it could track the average diameter of the clusters. This factor would rise moderately during the clustering. But if a big jump is observed, it means that this is a point to stop the algorithm. Note that in this rule, you may not fix a threshold, you consider the trend and stop when something unusual happens.

### K-Mean Clustering
It is to group similar points into K clusters. More explanation [here](https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/)
Steps:
1.  Define the number of K clusters
2.  choose K random points as centroid. Each cluster has one centroid
3.  Assign all the points to the nearest centroids
4.  recompute the newly formed clusters
5.  repeat 3 and 4 
When to stop:
1.  Centroids of newly formed clusters do not change
2.  Points remain in the same cluster
3.  Maximum number of iterations are reached

### Structure of the Web (shown in picture structure_of_web.png)
It includes :
1.  In, nodes that can reach the giant SCC but cannot be reached from it e.g. new web pages, and
2.  SCC (Strong Connected Components). a strongly connected component is a region from which you can get from any point to any other point along a directed path. So in the context of the web graph, with this giant SCC, what this means is that from any webpage inside this blob, you can get to any other webpage inside this blob, just by traversing a sequence of hyperlinks.
3.  Out, nodes that can be reached from the giant SCC but cannot reach it e.g. corporate websites.
4.  Tendrils: the nodes reachable from IN that can’t reach the giant SCC, and the nodes that can reach OUT but can’t be reached from the giant SCC. If a tendril node satisfies both conditions then it’s part of a tube that travels from IN to OUT without touching the giant SCC, and

### Web Crawler
Web Crawler is one of the most used page ranking in the past in recent years, but large scale search engine like Goole use not only Web Crawler. there are rules to follow to Web Crawler

### Page Rank
The higher the page rank of a page, the higher the importance of the page is. Think of the web as a directed graph, each pages are nodes and the arcs between nodes are the link between them. each step a random surfer moves from current page to a randomly chosen page that it links to.

Refer to /PageRank_formula.png and below is the explanation.
where |G| is the total number of nodes (pages) in the graph, α is the random jump
factor, L(n) is the set of pages that link to n, and C(m) is the out-degree of node m
(the number of links on page m). The random jump factor α is sometimes called the
“teleportation” factor; alternatively, (1 − α) is referred to as the “damping” factor.
Let us break down each component of the formula in detail. First, note that
PageRank is defined recursively—this gives rise to an iterative algorithm we will detail
in a bit. A web page n receives PageRank “contributions” from all pages that link to
it, L(n). Let us consider a page m from the set of pages L(n): a random surfer at
m will arrive at n with probability 1/C(m) since a link is selected at random from all
outgoing links. Since the PageRank value of m is the probability that the random surfer
will be at m, the probability of arriving at n from m is P(m)/C(m). To compute the

PageRank of n, we need to sum contributions from all pages that link to n. This is
the summation in the second half of the equation. However, we also need to take into
account the random jump: there is a 1/|G| chance of landing at any particular page,
where |G| is the number of nodes in the graph. Of course, the two contributions need to
be combined: with probability α the random surfer executes a random jump, and with
probability 1 − α the random surfer follows a hyperlink.

#### Markov Process
Markov process is stochastic, The property of being well described by a random probability distribution. This means it is a random process in which the future is independent on the past, given the present.
This transition probabibily (moving from current page to another after a single step) can be presented in a matrix. 
This Transition matrix describes what happen to the surfer after a single step. For a graph with N pages, the matrix has dimension of NxN. If there is a link between two nodes, value of that m(ij) is 1/k where k is the total number of outgoing links from j to i. if theres no link, m(ij) is 0. These value will fill in Transition matrix

the limiting distribution,v , is [1/n, .... 1/n]^T for the length of n. n = the matrix row and col. Already explained at Clustering section

Probability distribution for a location of a surfer can be described by column vector of length n. for each j columns of NxN matrix, the probability a surfer is at page j is the j's component. This probability is the idealised PageRank function

The limiting distribution vector v, an eigenvector.
[I dont understand](http://pi.math.cornell.edu/~mec/Winter2009/RalucaRemus/Lecture3/lecture3.html)

What to avoid when using PageRank:
1.  Dead end, the one that is not scc. To solve it, remove all the dead ends recursively
2.  Spider web  

[simpler explanation,read to understand more about PageRank](https://www.isical.ac.in/~debapriyo/teaching/datamining2014/slides/PageRank.pdf)
\

[Difference between Yahoo and Google search engine](https://www.searchenginejournal.com/google-and-yahoo-search-engine-technology-comparison/2267/#close)

### Problem comes when the Matrix consist of billions of nodes
It is important to multiply matrix a certain times or to multiply with a vector, however the matrix is huge. To address this issue, a software stack is develop to apply parallelism on larger scale application. It uses computing clusters-a group of connected nodes by ethernet or inexpensive switches. 
Each computing node consist of a processor and memory. This sofware stack is based on a file system called distributed file system. To be fault tolerant during computation, it creates multiple copies of the data. It also uses larger units than disc blocks in ordinary operation systems.

#### Map Reduce
Map reduce is one of the high level programming systems based on this file system. It helps to perform calculation with efficient time and deal with hardware failure well
[Here is how MapReduce works](https://courses.edx.org/assets/courseware/v1/12127e16fb054ef296141f8809f00193/asset-v1:AdelaideX+BigDataX+1T2021+type@asset+block/5_2_1-more-about-MapReduce.pdf)
[Here is the Book for MapReduce](https://lintool.github.io/MapReduceAlgorithms/MapReduce-book-final.pdf)

Combiner is a kind of reducer. Combiner is mainly used to reduce the size of data which is transferred between nodes. Combiner is not always run, your computer decides it. So, it is better to have combiner func and reducer and func the same or the same input and output type

##### Map Reduce for PageRank
Because pageRank uses matrix multiplication alot, we can use mapreduce to perform that. Explanation[ matrix multiplication with map reduce](https://www.geeksforgeeks.org/matrix-multiplication-with-1-mapreduce-step/) and picture /Matrix Matrix Multiplication with Mapreduce.png
when creating transition matrix in the process, there are alof of zeros values in the matrix, this is called Sparse matrix. So to avoid storing zeroes values, we store node, degree (how many branches out from the node), neighbour (where the branches going to).


### Word Importance in a collection of documents

[TF.IDF](https://towardsdatascience.com/how-important-are-the-words-in-your-text-data-tf-idf-answers-6fdc733bb066) is an important measure to jusge the importance of words in a document. which should belong to a collection of documents. It takes into account the occurrences of the word in the document itself and it combines it with occurences of this word in any other documents

Some terms of big data algorithm :
1.  Word Importance
2.  Hash functions
3.  Indexes
4.  Secondary storage

To find the similarities between documents, use Jaccard similarity. it compares character to character and word by word. another way to find similarities between documents is Cosine similarity. it calculates the dot product of the two documents. Result of 1 being exactly the same and 0 being the total opposite

[Jaccard Similarity ith K Shingels](https://www.cs.utah.edu/~jeffp/teaching/cs5955/L4-Jaccard+Shingle.pdf)

To make the words in document into sets, K Shingels is used. K Shingels can be formed by words or characted

Now, in big data we are dealing with alot of data with alot of sets in the form ot character or words. When computing the union of different sents, you need to load all these sets and compute the intersection and union sized for each paris. Instead of dealing with such a large sets, which requires a lot of computing time and memory, MinHash can provide a sketch to approximate this measure in a scalable way. 
[MinHash](https://aksakalli.github.io/2016/03/01/jaccard-similarity-with-minhash.html) is a mechanism that can be used to estimate the similarity of two sets witha lesser memory space and in a more efficient way. It is done by using hashing/mapping function that typically reorders the elemts using simple math operation. MinHash has a surprising property, according to which, the probability that the MinHash of random permutation produces the same value for the two sets equals the Jaccard Similarity Coefficient of those sets.

After getting the Signature Matrix from MinHash, we can use Local-Sensitive Hashing (LSH). More example [here](https://medium.com/carbon-consulting/explaining-lsh-minhash-simhash-c3cc33040030) and [here](https://towardsdatascience.com/understanding-locality-sensitive-hashing-49f6d1f6134)
and this is a [video](https://www.youtube.com/watch?v=96WOGPUgMfw) of more detailed explanation of MinHash

#### Association rules
More explanation [here](https://towardsdatascience.com/association-rule-mining-be4122fc1793)
It is defined to be corelation between X -> Y. X being sets of items that is related to item Y
Concepts of association rules:
1.  Confidence
2.  Support
3.  Lift

[A-priori Algorithm](https://www.geeksforgeeks.org/apriori-algorithm/) is an algorithm to compute frequent items. It is very efficient. It is done by these observations:
1.  itemset is frequent
2.  support of an itemset never exceeds the support of its subset.
3.  threshold will be 1% of the basket.
a-priori algorithm from scratch https://www.youtube.com/watch?v=2oVMmMdeCOQ

#### Movie and music recommendations

##### Collaborative filtering recommending systems
the approach is to look at users that are similar to the targetted user. The idea is that users who are similar will like the movies that they havent seen but that similar user has liked. A recommendation for a user U is made based on users that are most similar to U and recommending items that these users liked.  You can use Jaccard similarity ti fins the similar users.

Rating matrix is usually sparse because the watched movies are much lesser than total movies. This makes it hard to do a recommendation as theres not much information that we can based our decision on when considering rating matrix. Here we can use clustering to improve the procedure of finding recommendation to make the matrix less sparse.
1.  We can group single movies into a super movie e.g a series of single movies (thor, captain marvel, etc) into one (marvel). The rating will be the average of all marvel movies.
2.  We can group user by using your chosen clustering algorithm. Similarly, you can cluster users to super users and take the average among these users as the entry rating.
