#!/usr/bin/env python
# coding: utf-8

# In[25]:


import yfinance as yf
import numpy as np 
df = yf.download(["AAPL" , "CAT"],start = "2000-12-01", end = "2024-12-01")
df = np.log(1 + df['Close'].pct_change())
df
df.mean()
weights = [0.5,0.5]
def portfolio_return(weights):
    returns = np.dot(df.mean(),weights)
    return returns
df.cov()
def portfolio_variance(weights):
    pv = np.dot(np.dot(df.cov(),weights),weights)
    return pv
def portfolio_std(weights):
    std = portfolio_variance(weights)**0.5*np.sqrt(250)
    return std 
def weightscreator(df):
    rand = np.random.random(len(df.columns))
    rand = rand/rand.sum()
    return rand
returns = []
stds = []
w = []
for i in range(500):
    weights = weightscreator(df)
    returns.append(portfolio_return(weights))
    stds.append(portfolio_std(weights))
    w.append(weights)

import matplotlib.pyplot as plt
plt.scatter(stds,returns)
plt.title("Efficient frontier")
plt.xlabel("Portfolio std")
plt.ylabel("Portfolio Returns")
plt.scatter(min(stds),returns[stds.index(min(stds))],c = "red")
plt.show 

    
            

    


# In[ ]:





# In[ ]:




