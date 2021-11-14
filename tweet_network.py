

import networkx as nx
from tweets_data import get_tweets



## Create retweets Subset of ds_tweets

ds_retweets = get_tweets()

G_rt = nx.from_pandas_edgelist(
    ds_retweets,
    source = "user-screen_name",
    target = "retweeted_status-user-screen_name",
    create_using = nx.DiGraph())
 
# Print the number of nodes
print('Nodes in RT network:', len(G_rt.nodes()))

# Print the number of edges
print('Edges in RT network:', len(G_rt.edges()))



## Create reply Subset of ds_tweets

ds_replies = get_tweets()

# Create reply network from edgelist
G_reply = nx.from_pandas_edgelist(
    ds_replies,
    source = "user-screen_name",
    target = "in_reply_to_screen_name",
    create_using = nx.DiGraph())
    
# Print the number of nodes
print('Nodes in reply network:', len(G_reply.nodes()))

# Print the number of edges
print('Edges in reply network:', len(G_reply.edges()))



## Drawing the Graph

pos = nx.random_layout(G_rt)

# Create size list
sizes = [x[1] for x in G_rt.degree()]


# Draw the network
nx.draw_networkx(G_rt, pos, 
    with_labels = False, 
    node_size = sizes,
    width = 0.1, alpha = 0.7,
    arrowsize = 2, linewidths = 0)

# Turn axis off and show
plt.axis('off'); plt.show()



## Nodes Of Interest 

# Generate in-degree centrality for retweets 
rt_centrality = nx.in_degree_centrality(G_rt)

# Generate in-degree centrality for replies 
reply_centrality = nx.in_degree_centrality(G_reply)

# Store centralities in DataFrame
rt = pd.DataFrame(list(rt_centrality.items()), columns = column_names)
reply = pd.DataFrame(list(reply_centrality.items()), columns = column_names)

# Print first five results in descending order of centrality
print(rt.sort_values('degree_centrality', ascending = False).head())

# Print first five results in descending order of centrality
print(reply.sort_values('degree_centrality', ascending = False).head())



rt_centrality = nx.betweenness_centrality(G_rt)

# Generate betweenness centrality for replies 
reply_centrality = nx.betweenness_centrality(G_reply)

# Store centralities in data frames
rt = pd.DataFrame(rt_centrality.items(), columns = column_names)
reply = pd.DataFrame(reply_centrality.items(), columns = column_names)

# Print first five results in descending order of centrality
print(rt.sort_values('betweenness_centrality', ascending = False).head())

# Print first five results in descending order of centrality
print(reply.sort_values('betweenness_centrality', ascending = False).head())
