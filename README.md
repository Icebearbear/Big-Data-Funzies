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