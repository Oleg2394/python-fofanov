#!/usr/bin/env python
# coding: utf-8

# In[1]:


def hello_world():
    print("Hello, world")
hello_world()    


# In[3]:


hello2 = hello_world
hello2


# In[4]:


hello2()


# In[ ]:





# In[5]:


def hello_world():
    def internal():
        print("Hello, world!")
    return internal    


# In[7]:


hello2 = hello_world()
hello2


# In[ ]:





# In[8]:


def say_something(func):
    func()

def hello_world():
    print("Hello, world!")

say_something(hello_world)    


# In[ ]:





# In[12]:


def loh_decorator(func):
    def wrap():
        print(f"cALLING FUNC {func}")
        func()
        print(f"Func {func} finiched is workd")
    return wrap    


# In[13]:


def hello():
    print("Hello, world")
    


# In[14]:


wrapped_by_logger = loh_decorator(hello)
wrapped_by_logger()


# In[ ]:





# In[16]:


@loh_decorator
def hello():
    print("hello, world")


# In[17]:


hello()


# In[ ]:





# In[18]:


from timeit import default_timer as timer
import math
import time


# In[19]:


def measure_time(func):
    def inner(*args, **kwarks):
        start = timer()
        
        func(*args, **kwarks)
        
        end = timer()
        
        print(f"Время работы функции {func.__name__} {end-start}")
    return inner


# In[20]:


@measure_time
def factorial(num):
    time.sleep(3)
    print(math.factorial(num))


# In[22]:


factorial(100)


# In[ ]:





# In[ ]:




