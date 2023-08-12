#!/usr/bin/env python
# coding: utf-8

# In[5]:


#need of giving mutiple variables one value
suman= sadhna = roshini="pakistani"
print(suman+" "+sadhna+" "+roshini)

#dont make a mistake like this 
#suman, sadhna , roshini="pakistani"
#this will give error of too many values to unpack


# In[11]:


#when we a a list and divide it into multiple variables  sequence wise 
Jobs=["assistant director", "Director ", "producer"]
suman, sandiya, arzu = Jobs
print(suman+" "+sandiya+" "+arzu)


# In[15]:


#concation of string and number is not possible without typecasting 
#print("suman"+2)  #its an error


# In[19]:


#global variable is defined outside the function 
year = "2023"
def current_year():
    print("current year is "+ year)
current_year()

#global variable is accesible both outside and inside function
print("current year is "+ year)


# In[23]:


#local variable (variable inside function)
def Current_year():
    Year ="2023"
    print("current year is "+Year)
Current_year()
#local variable is not accesible  outside the function
#print("current year is "+Year) #error


# In[33]:


#using keyword global to make local variable global 
def Location():
    global location
    location="lahore"
    print("today's match location is :"+location)
Location()
#wohooo we made a local varibale global
print("today's match location is :"+location)

