#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup


# In[2]:


link = 'http://quotes.toscrape.com/'


# In[3]:


res = requests.get(link)


# In[4]:


soup = BeautifulSoup(res.text, 'html.parser')


# In[5]:


print(soup.find('span', class_= 'text').text[1:-1])


# In[6]:


quotes = []

for quote in soup.find_all('span', class_= 'text'):
    quotes.append(quote.text[1:-1])


# In[7]:


quotes


# In[8]:


data = []

for sp in soup.find_all('div', class_ = 'quote'):

    quote     = sp.find('span', class_ = 'text').text[1:-1]
    author    = sp.find('small').text
    author_id = sp.find('a').get('href')
    
    tags = []
    for tag in sp.find_all('a',class_ = 'tag'):
        tags.append(tag.text)
    tags      = ','.join(tags)

    data.append([quote, author, author_id, tags])


# In[9]:


data[0]


# In[17]:


data = []

for page in tqdm(range(1, 11)):
    link = "https://quotes.toscrape.com/page/" + str(page)
    res =  requests.get(link)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    for sp in soup.find_all('div', class_ = 'quote'):

        quote     = sp.find('span', class_ = 'text').text[1:-1]
        author    = sp.find('small').text
        author_id = sp.find('a').get('href')

        tags = []
        for tag in sp.find_all('a',class_ = 'tag'):
            tags.append(tag.text)
        tags      = ','.join(tags)

        data.append([quote, author, author_id, tags])


# In[18]:


len(data)


# In[19]:


df = pd.DataFrame(data, columns = ['quote','author','author_id','tags'])


# In[20]:





# In[21]:


df


# In[14]:


author_id=sp.find('a').get('href')


# In[15]:


tags = []

for tag in sp.find_all('a', class_= 'tag'):
    tags.append(tag.text)


# In[16]:


','.join(tags)


# In[24]:


df['author_link']='https://quotes.toscrape.com' + df['author_id']


# In[25]:


df


# In[26]:


df.to_csv('Quotes.csv', index = False)


# In[ ]:




