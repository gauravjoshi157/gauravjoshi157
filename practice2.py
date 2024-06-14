# program to find the sum of square of first n number 
def sum_of_serie(n):
    sum = 0 
    for i in range(1, n + 1):
        sum += i * i
    return sum
x =int(input("enter the value of n:"))
print(sum_of_serie(x))
        
        
        
# program to find the sum of cube of first n number 
def sum_of_serie(n):
    sum = 0 
    for i in range(1, n + 1):
        sum += i * i*i
    return sum
x =int(input("enter the value of n:"))
print(sum_of_serie(x))
        
          
# program to find ASCII value of the character
x ="a"
print("The ASCII value of '" + x + "' is", ord(x))


# program to find the sum of array element
def sum(arr):
    sum = 0
    for i in arr:
        sum = sum+i
    return (sum)
arr = [12, 3, 4, 15]
print("the sum of array element is :",sum(arr))


# program to find largest number in the array element
def largest_number(arr,n):
    ans = max(arr)
    return ans
arr = [12, 3, 4, 15]
n = len(arr)
print("the sum of the array is:",largest_number(arr,n))



def swap(new_list):
    size = len(new_list)
    temp = new_list[0]
    new_list[0] = new_list[size-1]
    new_list[size-1] = temp
    return new_list
list1 = [12, 3, 4, 15]
x = swap(list1)
print(x)



# program to find difference between two dates
from datetime import date
date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)
difference = date2-date1
print(difference)
   
   
   
# Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference
def difference(n):
    if 17 <=n:
        return (n-17)*2
    else :
        d=17-n 
        return d
y= int(input("Enter the number:"))
print(difference(y))
 
 
 
 
 
 #program to find volume of a sphere of radius r
import math
def volume(r):
    v=(4/3)*math.pi*r*r*r
    return v 
r = int(input("enter the radius"))
print(volume(r))



 # Python program to test whether a number is within 100 of 1000 or 2000. 

def near_thousand(n):
    return ((abs(1000-n)<=100) or (abs(2000-n)<=100))

print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(1200))



# Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
n1=int(input("entr the first number :"))
n2=int(input("entr the second number :"))
n3=int(input("entr the third number :") )
if (n1==n2==n3):
     print(n1*3*3)
else :
    print(n1+n2+n3)
    
    
    
    
#Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is"
def new_string(text):
    if ((len(text)>=2) and (text[:2]=="IS")):
        return text
    else :
        return "IS"+text

x = str(input("input the string"))
print(new_string(x))
        
    

              
