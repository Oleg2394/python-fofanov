#!/usr/bin/env python
# coding: utf-8

# In[1]:


greeting = "Hello from global scope"

def greet():
    greeting = "Hello from enclosing scope"
    
    def nested():
            greeting = "Hello from local scope"
            print(greeting)
    nested()        


# In[2]:


greet()
print(greeting)


# In[3]:


#list


# In[4]:


greeting = "Hello from global scope"

def greet(greeting):
    print(f"Greet in func: {greeting}")
    greeting = "Hello from enclosing scope"
    
    print(f"Greet in func:{greeting}")
    
    def nested():
        greeting = "Hello from local scope"
        print(greeting)
    nested()    


# In[5]:


greet("test")
print(greeting)


# In[ ]:





# In[10]:


greeting = "Hello from global scope"

def greet():
    global greeting
    print(f"Greet in func: {greeting}")
    
    def nested():
        greeting = "Hello from local scope"
        print(greeting)
    nested()    


# In[11]:


greet()
print(greeting)


# In[ ]:




