#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np


# In[1]:


print("HelloWorld!")


# In[2]:


print("HelloWorld")


# In[3]:


A = 3
B = 3.1
C = True
D = "Kevin"
print(A)


# In[4]:


print(B)


# In[5]:


print(type(B))


# In[6]:


x1 = 2
x2 = 10
print(x1+x2)


# In[7]:


Z = x1 * x2
print(Z)


# In[8]:


input()


# In[9]:


input('Enter your name:')


# In[10]:


input('enter your first number: ')


# In[13]:


x = int(input('your first number'))
y = int(input('your second number'))
z = int(input('your third number'))

print("the total of the above inputs is equal to",x+y+z)


# In[14]:


print(not(3 > 9))


# In[18]:


X = 5
if X == 5: 
    print("x is equal to 5")
else:
    'x is not equal to 5'


# In[19]:



module1 = int(input('your first mark'))
module2 = int(input('your second mark'))

score = (module1 + module2)/2

if score >= 70:
    print('A')
elif score >= 60:
    print ('B')
elif score >= 50:
    print('C')
else:
    print ('F')


# In[27]:


for i in range(11):
    if (i%2==0):
        print(i)


# In[33]:


empl = [10000,20000,30000,40000]
print(empl)


# In[34]:


print(len(empl))


# In[35]:


print(empl[1])


# In[37]:


r = 10
c_area = r * r * 3.14
print(c_area)


# ### Functions

# In[41]:


def circle_area(r):
    result= r**2*3.14
    return result        


# In[42]:


circle_area(10)


# In[45]:


def summation(x,y):
    result = x + y
    return result


# In[46]:


summation(10,10)

