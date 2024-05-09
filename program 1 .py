#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[6]:


hours_studied = [10,9,2,15,10,16,11,16]
exam_scpres = [95,80,10,50,45,98,38,93]
plt.plot(hours_studied,exam_scpres, marker='*',color = 'red',linestyle='-')
plt.xlabel('Hours Studied')
plt.ylabel('Score in final exam')
plt.title('Effect of hours studied on exam score')
plt.show()

