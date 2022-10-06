#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello")


# In[2]:


#sum of two no's
a=10
b=10
c=a+b
print(c)


# In[4]:


#sum of two no's
a=input("enter value for a")
b=input("enter value for b")
c=int(a)+int(b)
print(c)


# In[8]:


#swapping
a=10
b=5

temp=a
a=b
b=temp
print("value of a is",a)
print("value of b is",b)


# In[9]:


#swapping
a=input("enter a")
b=input("enter b")
print("value of a before swap",a)
print("value of b before swap",b)
temp=a
a=b
b=temp
print("value of a after swap",a)
print("value of b after swap",b)


# In[29]:


#linear search
def ls(arr,n,x):
    for i in range(0,n):
        if (arr[i]==x):
            return i
    return -1
           
arr=[9,7,6,0,-1]
x=0
n=len(arr)
r=ls(arr,n,x)
if(r==-1):f = open("demofile3.txt", "r")
print(f.read())
Run Example »

    print("element not found")
else:
    print("element found at index",r)


# In[50]:


#binary search
def binarySearch(array, x, low, high):
    if high >= low:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)
        else:
            return binarySearch(array, x, mid + 1, high)
    else:
        return -1

array = [3, 4, 5, 6, 7, 8, 9]
x = 4
result = binarySearch(array, x, 0, len(array)-1)
if result != -1:
    print("Element is present at index " ,result)
else:
    print("Not found")


# In[43]:


#selection sort
def ss(arr,size):
    for i in range(size):
        minindex=i
        for j in range(i+ 1, size):
            if arr[j]<arr[minindex]:
                minindex=j
        (arr[minindex],arr[i])=(arr[i],arr[minindex])
arr=[3,4,9,1,0]
size=len(arr)
ss(arr,size)
print(arr)
        


# In[48]:


#to open a file
f=open("temp.txt","w+")
#for i in range (10):
f.write("heloo ")#"%d \n" %(i+1))
f.close()
#f = open("sushmitha.txt", "r")
#print(f.read())


# In[24]:


#mean
num=[1,2,3,4,5,6,7,8,9,10]
n=len(num)
meanans=sum(num)/n
print(meanans)


# In[13]:


#median
data=[21, 13, 19, 3,11,5]
data.sort()

n=len(data)
if n%2==0:
    firstmed=data[n//2]
    secmed=data[(n+1)//2-1]
    median=(firstmed+secmed)//2
else:
    median=data[n//2]
print("median is",median)


# In[20]:


#mode
def modef(nums):
    freq={}
    for i in nums:
        freq.setdefault(i,0)
        freq[i]+=1
    print(freq)
    maxfreq=max(freq.values())
    print(maxfreq)
nums=[1,2,3,3,3,3,2,1]
modef(nums)


# In[3]:


#varience
lis=[1,2,3,4,5]
n=len(lis)
mean=sum(lis)//n
var=0
for i in lis:
    var=var+(i-mean)**2
    varience=var//n
print(varience)


# In[4]:


#standard deviation
lis=[1,2,3,4,5]
n=len(lis)
mean=sum(lis)//n
var=0
for i in lis:
    var=var+(i-mean)**2
    Sd=(var//n)**0.5
print(Sd)


# In[23]:


#standardization
lis=[1,2,3,4,5]
mean1=sum(lis)//len(lis)
print("mean",mean1)
var=0
for i in lis:
    var=var+(i-mean)**2
    Sd=(var//n)**0.5
print("standard deviation",Sd)
for j in lis:
    standardization=(j-mean1)/Sd
    print(standardization)


# In[20]:


#normalization
lis=[1,2,3,4,5]
minimum=min(lis)
print("minimum element is",minimum)
maximum=max(lis)
print("maximum element is",maximum)
for i in lis:
    norm=(i-minimum)/(maximum-minimum)
    print(norm)
    type(file)


# In[37]:


#extracting features from csv file
import csv
file=open('/home/ignis/Documents/sush.csv')
csvreader = csv.reader(file)
row=[]
for i in csvreader:
    row.append(i)
row


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




