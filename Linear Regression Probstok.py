#!/usr/bin/env python
# coding: utf-8

# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0,10.0)

df1 = pd.read_csv(r"C:\Users\Nicholas\Desktop\Data Probstok\DelayedFlightshuh.csv")
print(df1.shape)
df1.head()


# In[43]:


#menentukan nilai x dan y
Y = df1['AirTime'].values
X = df1['TotalDelay'].values


# In[44]:


#membuat garis regresi
mean_x = np.mean(X)
mean_y = np.mean(Y)

m =len(X)

numer = 0
denom = 0
for i in range(m):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
b1 = numer / denom
b0 = mean_y - (b1 * mean_x)

print(b1, b0)


# In[45]:


#grafik
max_x = np.max(X) + 100
min_x = np.min(X) - 100

x = np.linspace(min_x, max_x, 1000)
y = b0 + b1 * x

plt.plot(x, y, color='#58b970', label='Regression Line')
plt.scatter(X,Y, color='#ef5423', label='Scatter Plot')

plt.xlabel('Total Delay')
plt.ylabel('Airtime')
plt.legend()
plt.show()


# In[46]:


#menentukan nilai R kuadrat
ss_t = 0
ss_r = 0
for i in range(m):
    y_pred = b0 + b1 * X[i]
    ss_t += (Y[i] - mean_y) ** 2
    ss_r += (Y[i] - y_pred) ** 2
r2 = 1 - (ss_r/ss_t)
print(r2)


# In[ ]:





# In[ ]:




