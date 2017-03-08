
# coding: utf-8

# In[1]:

def vol_sphere(rad):
    print ((4*3.14*rad**3)/3)
vol_sphere(3)


# In[2]:

def ran_check(num,low,high):
    if num>=low and num<=high:
        print("Yes number is in range")
    else:
        print("NUmber is not is range")
ran_check(4,3,6)


# In[4]:

def unique_list(l):
    result = list(set(l))
    return result
print(unique_list([1,1,1,2,2,3,4,3,5,5,4,6]))


# In[7]:

def multiply(numbers):
    result=1
    for i in range(len(numbers)):
        result=result*numbers[i]
    return result
print (multiply([1,4,6,-7]))


# In[13]:

def palindrome_bool(s):
    s1=s[::-1] #reverse the string
    if(s1 == s):
        return True
    else:
        return False
print(palindrome_bool('helleh'))


# In[15]:

print(palindrome_bool('hello olleh'))


# In[36]:

import string
def pangram_bool(s,alpha=string.ascii_lowercase):
    alphaset=set(alpha)
    return alphaset<= set(s.lower())
pangram_bool("The quick brown fox jumps over the lazy dog")
  


# In[39]:

print(pangram_bool("abc def gha mno ijk lmnopq rst u v wxyz"))


# In[35]:

def up_low(s):
    d={"upper":0,"lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print(d["upper"]," <----upper case letters")
    print(d["lower"]," <----lower case letters")
up_low("Ankit Agrawal")
        

