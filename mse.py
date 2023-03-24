#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4,5])
y=np.array([2,50,4,5,7])

mx=np.mean(x)
my=np.mean(y)

print("x, y의 평균 값은",mx,"와 ",my)

plt.figure(figsize=(5, 3))
plt.scatter(x, y)
plt.show()


# In[25]:


divisor=sum([(i-mx)**2 for i in x]) #iterable한 자료형을 받음. 배열의 원소들을 순환하여 저장

def top(x,mx,y,my):
    d=0
    for i in range(len(x)):
        d+=(x[i]-mx)*(y[i]-my)
    return d
dividend=top(x,mx,y,my)

a=dividend/divisor #weight
b=my-(mx*a) #bias

print("y = ", a,"x + ",b) #최소제곱법으로 함수 구함. 



# In[26]:


predict_result=[]

def predict(x): #평균오차계산
    return a*x+b
for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print("study time = %.f, real grade = %.f, predicted grade = %.f" %(x[i], y[i], predict(x[i])))
    
n=len(x)
def mse(y,y_pred):
    return (1/n)*sum((y-y_pred)**2)

print("평균 제곱 오차: "+str(mse(y,predict_result)))
    


# In[ ]:





# In[ ]:




