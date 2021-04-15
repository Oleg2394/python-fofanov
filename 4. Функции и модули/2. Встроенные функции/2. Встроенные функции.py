#!/usr/bin/env python
# coding: utf-8

# In[1]:


abs(-1) # Взять число по модулю


# In[2]:


abs(1) # Взять число по модулю


# In[3]:


max(1,2,3,4,5) # Поиск максимума


# In[5]:


min([1,2,3,4,5]) # Поиск минимума по списку


# In[6]:


pow(2,8) # Возведение в степень


# In[7]:


round(3.37,1) # Округление до 1 знака


# In[9]:


sum([1,2,3,4,5]) # Сумма чисел только по списку


# In[10]:


h = hex(42) # десятичное число в 16 ричное
o = oct(42) # десятичное число в 8 ричное
b = bin(42) # десятичное число в 2 ичной

print(h)
print(o)
print(b)


# In[ ]:





# In[11]:


all_true1 = all([True,True,True]) # Проверка что все значения равно true
all_true2 = all([True,False,True]) # Проверка что все значения равно true

print(all_true1)
print(all_true2)


# In[12]:


players = [("Carlsen", 2842), ("Caruana", 2822),
          ("Mamedyarov", 2801), ("Bing", 2797)]


# In[13]:


all(rating > 2700 for _, rating in players)


# In[14]:


all(rating > 2800 for _, rating in players)


# In[16]:


all([rating > 2800 for _, rating in players])


# In[ ]:





# In[17]:


any_true1 = any([False,False,True]) # Если хотябы один true то все выражение в true
any_true2 = any([False,False,False])

print(any_true1)
print(any_true2)


# In[20]:


any(rating < 2790 for _, rating in players)


# In[21]:


any(rating < 2700 for _, rating in players)


# In[ ]:





# In[22]:


letters = 'abcd'
numbers = (10,20,30)

zipped = zip(letters,numbers) # Склейка списков
print(type(zipped))
print(zipped)

zipped_list = list(zipped)
print(zipped_list)


# In[23]:


names = ["Carlsen", "Caruana", "Mamedyarov", "Ding", "Giri"]
rating = [2842,2822,2801,2797,2780]

players = dict(zip(names, rating))
players


# In[ ]:





# In[24]:


reply = input("Введите слово") # Ввод текста
reply


# In[ ]:





# In[25]:


code = ord("a") # Вывод unicode таблицы
code


# In[26]:


c = chr(code) # Вывод из unicode таблицы в значение
c


# In[ ]:




