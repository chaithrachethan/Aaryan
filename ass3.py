
1. Python program to print first n prime numbers where n is the input
sol:
i = 1
x = int(input("Enter the number:"))
for k in range(1, x+1):
    c = 0
    for j in range(1, i+1):
        a = i % j
        if a == 0:
            c = c + 1

    if c == 2:
        print(i)
    else:
        k = k - 1

    i = i + 1
    
2. Python Program to remove duplicate elements from a list WITHOUT using set
soln:


list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
 
new = []  
 
for a in list:
    n = list.count(a)
    if n > 1:
 
        if new.count(a) == 0: 
 
            new.append(a)
 
print(new)
          
       


33. Filter the price in a dictionary, check if the price of the item is 
	greater than 2000, between 3000-7000 and so on
	Ex: 
		smart_phone_dict =  {'Samsung': 35500, 'Realme': 14000, 'Moto G10 Power': 3500, 'OnePlus 8 Pro':50000, 'Samsung 2': 6000, 'Lika': 1500
		, 'Lava': 2500,  'Redme': 4500}

s_dict =  {'Samsung': 35500, 'Realme': 14000, 'Moto G10 Power': 3500, 'OnePlus 8 Pro':50000, 'Samsung 2': 6000, 'Lika': 1500
		, 'Lava': 2500,  'Redme': 4500}
n_dict = dict()

for (key, value) in s_dict.items():
    if value>2000 and value<7000:
        n_dict[key]=value

print(n_dict)