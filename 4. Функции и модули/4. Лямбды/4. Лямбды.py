#!/usr/bin/env python
# coding: utf-8

# In[1]:


def square(*args):
    return [x*x for x in args]


# In[2]:


result = square(1,2,3,4,5)
result


# In[ ]:





# In[3]:


def triple(*args):
    return [x*3 for x in args]


# In[4]:


result = triple(1,2,3,4,5)
result


# In[ ]:





# In[6]:


def square(number):
    return number * number

numbers = [1,2,3,4,5]

mapped_seq = map(square,numbers) # Применение к одному списку попереемнной элементы второго


# In[7]:


for x in map(square, numbers):
    print(x)


# In[8]:


print(type(mapped_seq))


# In[9]:


list(map(square,numbers))


# In[ ]:





# In[13]:


def is_adult(age):
    return age >= 18

ages = [14,18,21,16,30]


# In[14]:


filter(is_adult,ages) # filter Фильтр по условию


# In[15]:


list(filter(is_adult,ages))


# In[ ]:





# In[16]:


is_adult =  lambda age: age >= 18


# In[17]:


list(filter(is_adult,ages))


# In[18]:


list(filter(lambda age: age >= 18,ages))


# In[19]:


miltipliter = lambda x, y: x * y


# In[20]:


miltipliter(2,3)


# In[ ]:




