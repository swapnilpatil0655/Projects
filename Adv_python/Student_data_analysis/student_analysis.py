#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df=pd.read_csv("Expanded_data.csv")
df


# In[25]:


df=pd.read_csv("Expanded_data.csv")
print(df.head())


# In[26]:


df.describe()


# In[27]:


df.info()


# In[29]:


df.isnull().sum()


# # Drop unnamed column

# In[30]:


df=df.drop("Unnamed: 0",axis=1)
print(df.head())


# In[19]:


df.isnull().sum()


# In[21]:


print(df.head())


# # gender distribution

# In[44]:


plt.figure(figsize=(5,5))
ax=sns.countplot(data=df,x="Gender")
ax.bar_label(ax.containers[0])
plt.title("Gender Distribution")
plt.show

# from the above chart we have analysed that:the number of females in the data is more than the number of males
# In[48]:


gb=df.groupby("ParentEduc").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
print(gb)


# In[60]:


plt.figure(figsize=(4,4))
sns.heatmap(gb,annot=True)
plt.title("Relationship between Parent's Education and student's Score")
plt.show()

#from the above chart we have conclude that the education of the parents have good impact on their scores
# In[57]:


gb1=df.groupby("ParentMaritalStatus").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
print(gb)


# In[61]:


plt.figure(figsize=(4,4))
sns.heatmap(gb1,annot=True)
plt.title("Relationship between Parent's Marital Status and student's Score")
plt.show()

#from the above chart we have concluded that there is no/negligible impact on the
#student's score due to their parent's marital status
# In[49]:


sns.boxplot(data=df,x="MathScore")
plt.show()


# In[50]:


sns.boxplot(data=df,x="ReadingScore")
plt.show()


# In[51]:


sns.boxplot(data=df,x="WritingScore")
plt.show()


# In[68]:


print(df["EthnicGroup"].unique())


# # Distribution of Ethnic Groups

# In[91]:


groupA=df.loc[(df["EthnicGroup"]=="group A")].count()
groupB=df.loc[(df["EthnicGroup"]=="group B")].count()
groupC=df.loc[(df["EthnicGroup"]=="group C")].count()
groupD=df.loc[(df["EthnicGroup"]=="group D")].count()
groupE=df.loc[(df["EthnicGroup"]=="group E")].count()

l=["group A","group B","group C","group D","group E"]
mylist = [groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]

print(mylist)
plt.pie(mylist, labels=l, autopct = "%1.2f%%" )
plt.title("Distribution of Ethnic Groups")
plt.show()


# In[129]:


ax = sns.countplot(data = df,x = "EthnicGroup")
ax.bar_label(ax.containers[0])


# In[130]:


groupA=df.loc[(df["EthnicGroup"]=="group A")].count()
groupB=df.loc[(df["EthnicGroup"]=="group B")].count()
groupC=df.loc[(df["EthnicGroup"]=="group C")].count()
groupD=df.loc[(df["EthnicGroup"]=="group D")].count()
groupE=df.loc[(df["EthnicGroup"]=="group E")].count()

l=["group A","group B","group C","group D","group E"]
mylist = [groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]

print(mylist)
plt.pie(mylist, labels=l, autopct = "%1.2f%%" )
plt.title("Distribution of Ethnic Groups")
plt.show()


# # Distribution of Practice Sport

# In[133]:


print(df["PracticeSport"].unique())


# In[28]:


gb2=df.groupby("PracticeSport").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
print(gb2)


# In[48]:


plt.figure(figsize=(4,4))
sns.heatmap(gb2,annot=True)
plt.title("Relationship between Practice Sport Status and student's Score")
plt.show()

# from the above chart we have concluded that student who is involve in any practice storts they are getting more scores in the exam.
# In[47]:


reg=df.loc[(df["PracticeSport"]=="regularly")].count()
sometimes=df.loc[(df["PracticeSport"]=="sometimes")].count()
never=df.loc[(df["PracticeSport"]=="never")].count()

print("Regular : ",reg["PracticeSport"])
print("Sometimes : ",sometimes["PracticeSport"])
print("Never : ",never["PracticeSport"])


# In[52]:


reg=df.loc[(df["PracticeSport"]=="regularly")].count()
sometimes=df.loc[(df["PracticeSport"]=="sometimes")].count()
never=df.loc[(df["PracticeSport"]=="never")].count()

p=["Regularly","Sometimes","never"]
ps=[reg["PracticeSport"],sometimes["PracticeSport"],never["PracticeSport"]]

print(ps)
plt.pie(ps,labels=p,autopct="%1.2f%%")
plt.title("Distribution of Practice Sports")
plt.show()


# In[53]:


ax = sns.countplot(data = df,x = "PracticeSport")
ax.bar_label(ax.containers[0])

#Students practicing sports sometimes are in greater numbers than regular and never