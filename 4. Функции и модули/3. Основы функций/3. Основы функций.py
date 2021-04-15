#!/usr/bin/env python
# coding: utf-8

# In[1]:


def greeting():
    print("Hello!")


# In[2]:


greeting()


# In[3]:


greeting


# In[4]:


help(greeting)


# In[ ]:





# In[5]:


def greeting():
    """
    Документация на функцию:
    Input: Входные данные
    Output: Выходные данные
    """
    print("Hello!")


# In[6]:


help(greeting)


# In[ ]:





# In[7]:


def print_name(name): # Функция с аргументом
    print(name)


# In[8]:


print_name("Oleg")


# In[9]:


print_name()


# In[ ]:





# In[10]:


def print_name(name="Default"): # Функция с аргументом и значением по умолчанию
    print(name)


# In[11]:


print_name()


# In[ ]:





# In[12]:


result = print_name()
print(result)
print(type(result))


# In[ ]:





# In[13]:


def get_greting(name): # Функция с аргументом и возвращаемым значением
    return "Hello " + name

gre = get_greting("Oleg")
gre


# In[14]:


def get_sum(a,b):
    return a + b

result = get_sum(10,2)
result


# In[15]:


def is_adult(age):
    return age >=18

is_adu = is_adult(20)
is_adu


# In[16]:


def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("aabaa"))
print(is_palindrome("aabba"))


# In[ ]:





# In[17]:


def cals_taxes(p1,p2,p3):
    return sum((p1,p2,p3) * 0.06


# In[18]:


cals_taxes(10,20,30)


# In[20]:


def cals_taxes(p1,p2,p3,p4):
    return sum((p1,p2,p3,p4)) * 0.06


# In[21]:


cals_taxes(10,20,30,40)


# In[ ]:





# In[22]:


def cals_taxes(*args): # *args любое количество аргументов
    for x in args:
        print(f"Got payment = {x}")
    return sum(args) * 0.06   


# In[24]:


cals_taxes(10,20,30,40)


# In[ ]:





# In[28]:


def save_players(**kwargs): # *kwargs любое количество аргументов пара ключ значение (словарь)
    for k, v in kwargs.items():
        print(f"Players {k} has rating {v}")
                                 
save_players(Carlsen=2800, Giri=2780)    


# In[ ]:





# In[ ]:


# def func_important(a,b,c,d, *args, **kwargs)

