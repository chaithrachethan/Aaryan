"""
1. Write a function to find sum of the list elements
	Ex: Input [12,2,46]
	output = 60
sol: 
def add(a,b,c):
    sum_of_3=a+b+c
    return sum_of_3
x=(add(12,2,46))
print(x)
2. Write a function to count the number of times a letter appered in a word
	example: p count in apple is 2
	input word, letter
	output count
sol:
txt="letter"
x=txt.count("t")
print(x)


3. Write a function to print positive numbers in a list
	Ex: Input [-12,2,46, -20, 40, -99, 33]
	output = [2,46,40,33]
    
sol:
list1 =  [-12,2,46, -20, 40, -99, 33]
for num in list1:
    if num >= 0:
        print(num,end = " ")
        
4. Wite a function to print empty elemets in list
	Ex: Input [apple, '', 123, [], 22, 45, -30, None]
	output = [apple, 123, 22, 45]
sol:

my_list = ["apple", '', "123", [], "22", "45", "-30", "None"]
print("original list is :" + str(my_list))
for i in my_list :
    if(len(i)==0):
        my_list.remove(i)
print("modified list is :" + str(my_list))

5. Wite a function to print duplicate elements in the list
sol

x=[1,2,4,6,2,1]
print("original",x)
x=set(x)
print("set",x)
x=list(x)
print("list",x)

6. Wite a function to find second largest number in a list
sol

list1=[11,22,1,2,5,67,21,32]
new_list= set(list1)
new_list.remove(max(new_list))
print(max(new_list))
  or

list1=[11,22,1,2,5,67,21,32]
list1.sort()
print("second largest elements in the list is",list1[-2])


7. Write a function using list-comprehension to create a list of numbers which are divisible by 3
	example input [1, 3, 5, 9, 11, 12, 20, 15, 50, 33]
	output => [3,9,12,15,33]
sol:

number= [1, 3, 5, 9, 11, 12, 20, 15, 50, 33]
for x in number:
    if x % 3 ==0:
        print(x,end=" ")
        
8. Write a function to sort a list without using sort function
sol:        

number=[1,5,6,9,0]
for i in range(len(number)):
    for j in range(i+1,len(number)):
        if number[i]<number[j]:
            number[i],number[j]=number[j],number[i]
print(number)


9. Python function to convert Fahrenheit to Celsius
sol:

fahrenheit=54
celsius=((fahrenheit-32)*5)/9
print("temperature in celsius is:")
print(celsius)

10. Python function to remove  vowels in a given word
sol

str=input("enter string\n")
vowel_string="aeiouAEIOU"
str2=" "
print("input string\n",str)
for char in str:
    if char not in vowel_string:
        str2=str2+char
print("output string without vowels", str2)