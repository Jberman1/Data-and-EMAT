#!/usr/bin/env python
# coding: utf-8

# # Likes Report
# ## Jake Berman
# ### 9/21/21

# In[1]:


import pandas as pd
import json
import matplotlib as plt


# ## 1) 
# The cell below will open the json file and put the information into a variable called 'dat'.

# In[2]:


with open(r"/Users/jake/Downloads/jake___berman_20210907/likes/liked_posts.json") as p:
                dat = json.load(p)


# a) 'likes_media_likes is the only key to use.

# In[3]:


dat.keys()


# In[ ]:


dat['likes_media_likes']


# ## 2) 
# The cell below will convert the dictionary into a DataFrame.

# In[35]:


df_likes = pd.DataFrame(dat['likes_media_likes'])


# In[36]:


timestamp = [x['string_list_data'][0]['timestamp'] for x in dat['likes_media_likes']]


# In[37]:


df_likes['timestamp'] = timestamp


# b) The two lines above finds narrows the list down to timestamp and creates a column for it.

# In[29]:


df_likes


# ## 3)

# A) The data was collected from Instagram's algorithm.
# 
# B) Instagram collects the data about likes to try to show you ads that may be of interest to you, we collected the data to see how Instagram's algorithm keeps track of info on people's accounts.
# 
# C) The data is reliable because it is just tracking posts liked from my account so it is potential likes directly from the user.
# 
# D) The data may be unreliable for advertisers because liking a post doesn't necessarily mean that you are interested in it, so the data might not actually reflect the person's interests.

# ## 4) 
# The cell below groups the data by the 'title' or name of the account and tells us how many likes per account.

# In[39]:


df_likes.groupby('title').count()


# ## 5)

# ## Theoretical Hypothesis
# 
# a) I think that in the information about you folder the ads interests file will have unreliable data/have a bunch of ads that are of no interest to the user.
# 
# b) The ideal data for the hypothesis would be a file of all the ads clicked on by the user.

# ## Statistical Hypothesis
# 
# a) I think 90% of my the accounts from my liked posts will be from meme accounts.
# 
# b) The ideal data for the hypothesis would just be a statistic of the accounts from my liked posts to show what type of account they are.
# 

# ## 7)
# 
# The source of the data used was from Instagram. The structure of that data was in the form of lists. 

# In[45]:


df_likes.head(10)


# ## 9) 
# The cell above shows the first 10 likes, and the cell below shows the first 10 likes sorted by the title.

# In[48]:


df_likes.head(10).groupby('title').count()


# ## 10)
# That data shown is all collected from my personal instagram account and could potentially be used to show my interests based on the posts I have liked.

# ## 11)
# For alternative approaches I probably could of grouped the data by something other than title, like maybe timestamp to see the earliest likes rather than the number of likes by account name. I could also probably sort it by which account has the most likes. Although, I was not sure how to do that.
