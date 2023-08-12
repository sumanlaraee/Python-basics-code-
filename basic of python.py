#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#hey this is suman laraee 
#iam going to write code for basic syntax of python


# In[ ]:


#variable in python initialized direct
x=9
name ="suman laraee"


# In[3]:


#comments in python 
#single line comment starts with #
#comments used for increasing readibility, explaining code , preventing execution of particular code 
#python doesn't have multiline comment 
#we can use multiline comment by using string triplet quotes """

"""
hey you are coding
with suman laraee 
"""


# In[5]:


#type changing in python
age=90         #int
age="ninety"   #string
print(age)     #age is string now (Output: ninety )


# In[18]:


#type casting in python 
z=33

#converting integer to string by typecasting 

z=str(z)     #33 is string now '33'
print(type(z))    #class str     type() function is used to know type of variable 

#converting string to integer by typecasting 

z_=int(z)
print(type(z_))   #class int     type() function is used to know type of variable 


z__=float(z_)
print(type(z__))  #class float     type() function is used to know type of variable 


#name = "suman laraee"
#Name =int(name)
#print(Name)
#these three lines give error bcz string cannot be typecast into integer 


# In[19]:


#double and single quotes for string  both can be used no difference 
First_name ="suman"
Last_name='laraee'
print(First_name + " "+Last_name)


# In[24]:


#case Senstivity in python 
Age=9
age=900
print(Age , age )  #this is the method of printing multiple variables 
#Age wont overwrite age bcz python is case senstive there is difference btw A and a

#cannot print integer and string together bcz "" this is also string literal so both integers also giver error 
#print(Age+" "+age)

#sum of two integers 
print(Age+age)  #9+900=909


# In[ ]:


#multiple techniques to name variables 
#1:camelcase
myNameIs='suman laraee'
#2:pascalcase
MyNameIs="suman laraee"
#3:snakecase
my_name_is="suman"


# In[29]:


#variable name errors 
#1: cant begin with special signs 

# &name ="suman"  
# print(&name)   
#@name='suman'
#print(@name)

#2:cannot contain special signs in btw

#Name-1='suman'
#print(Name-1)

#3: can be alphanumeric (contain letters and numbers )
Name_2='suman bai'
print(Name_2)

#can start with underscore
_name="suman suman"
print(_name)


# In[30]:


#initializing many variables in one line 
name_1, name_2 ,name_3="suman", "sadhna", "roshni"
print(name_1+" "+name_2+" "+name_3)


# In[ ]:




