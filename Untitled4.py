#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np

num=int(input("Please provide no. of digits you want to print: "))

print(round(np.pi,num))


# In[9]:


decimal=int(input("Enter the no. you want to convert: "))
binary=bin(decimal).replace("0b", "")
decimal=int(binary,2)
print(binary)
print(decimal)


# In[13]:


cost=int(input("Enter the cost: "))
paid=int(input("Enter the paid amount: "))
change=paid-cost
print("You will get Rs "+ str(change)+ " in change AS:")
if change>0:
        rs_50=change//50
        rs_20=(change-(50*rs_50))//20
        rs_10=(change-(50*rs_50)-(20*rs_20))//10
        rs_5=(change-(50*rs_50)-(20*rs_20)-(10*rs_10))//5
        rs_2=(change-(50*rs_50)-(20*rs_20)-(10*rs_10)-(5*rs_5))//2
        rs_1=(change-(50*rs_50)-(20*rs_20)-(10*rs_10)-(5*rs_5)-(2*rs_2))
        if rs_50>0:
            print("no. of Rs 50 notes :"+ str(rs_50))
        if rs_20>0:
            print("no. of Rs 20 notes :"+ str(rs_20))
        if rs_10>0:
            print("no. of Rs 10 notes :"+ str(rs_10))
        if rs_5>0:
            print("no. of Rs 5 coins :"+ str(rs_5))
        if rs_2>0:
            print("no. of Rs 2 coins :"+ str(rs_2))
        if rs_1>0:
            print("no. of Rs 1 coins :"+ str(rs_1))
        
        


# In[47]:


def vowel_count(str):
    count=0
    vowel=set("aeiouAEIOU")
    for alphabet in str:
            if alphabet in vowel:
                count = count+1
    print("no. of vowels:", count)
    


fh=open("untitled.txt","r")
file_stuff=fh.read()
no=vowel_count(file_stuff)
print(no)
    
    


# In[64]:


import csv

with open("number.csv","r") as csv_file:
    csv_reader=csv.reader(csv_file)
    sorted_csv=sorted(csv_reader)
    for eachline in sorted_csv:
        print (eachline)
    
    


# In[65]:


class product:
    def __init__(self,price,Id,quantity):
        self.price=price
        self.Id=Id
        self.quantity=quantity
        
    def info(self):
        return str(self.Id)+" : "+str(self.quantity)+" : "+str(self.price)

product1=product(150,2,56)
print(product1.info())
        
             


# In[ ]:





# In[ ]:




