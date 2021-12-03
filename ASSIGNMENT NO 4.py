#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT 4

# In[ ]:


my_list = [ 'string', 'more string', 123, 99.9, True ] 
types = { type(item) for item in my_list } 

if int in types: 
    print('Found one!') 


# In[ ]:


d = {1.5,2.0};
print(d)
d.update({3.5});
print(d)


# In[ ]:


my_dict = {'data1':20,'data2':30,'data3':100};
print(sum(my_dict.values()))


# In[ ]:


list=[1,2,3,4,5,2,3,4,7,9,5];
list1=[];
for i in list:
    if i not in list1:
        list1.append(i)
    else:
        print(i,end=' ')


# In[ ]:


d = {1: 15, 2: 20, 3: 25, 4: 30, 5: 35, 6: 40};
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5);
is_key_present(9);


# In[ ]:


def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
print("select operation")
print("1. add ")
print("2. subtract ")
print("3. multiply ")
print("4. divide ")

while True:
    # take input from the user
    choice = input("enter choice(1/2/3/4):")
    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
             # check if user wants another calculation
        # break the while loop if answer is no
next_calculation = input("Let's do next calculation? (yes/no): ")
if next_calculation == "no":
          break
    
else:
        print("Invalid Input")
            
            


# In[ ]:





# In[ ]:




