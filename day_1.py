# a = 0 + 2j
# print(a)
# print(a.imag)
# print(a.real)


# slicing

# a = "abc\"xab"
# print(a)

# expo
# a = 1.534e+2
# print(type(a))
# print(a)

# name = "kavin prabhu"

# print(name[0:6])
# print(name[6:12])
# print(name[-6:])

# n = int(input("Enter the number:"))
# if (n%2==0):
#     print("Even")
# else:
#     print("Odd")

# a = 0.1
# a = 1
# a = 0
# print(bool(a))

# a = 0b10101
# print(a)
# print(type(a))
# print(hex(a))

# dict = {
#     "name":"mohan",
#     "age":21,
#     "active":True
# }
# print(dict)
# print(dict.keys())
# print(dict.values())

# print(dict["age"])

# List = [ [10,20,30,20 ],[1,2,3,4,5],["Mohan","Python.dev","Erode"]]
# print(List[0][3])
# print(List[1][1])
# print(List[2][2])

# a = range(10)
# # a = range(1,10)
# # a = range(10,100,5)
# print(a)
# for x in a:
#     print(x)

# l = [ 1,2,3,4,5,6,7,8,9]
# print(l)
# for x in l:
#     print(x)
# print(l[3])
# print(l[3:9])
# print(l.index(1))
# print(type(l))
# print(id(l))

# s = { "Mohan",10,24,True,"Python",10}
# print(s)
# print(id(s))
# s.add('Erode')
# print(type(s),len(s))
# print(s)
# print(id(s))
# b = frozenset(s)
# print(b)
# print(type(b))

# l3 = [12,"abc",True,False,1 + 0j]
# print(l3)
# l4 = l3[::-1]
# print(l4)

# for i in range(1,20):
#     print(i,end= " ")

# n = int(input("Enter N Number Table: "))
# for i in range(1,11):
#     print( i,"*",n ,"=" ,i*n )

# a = 15.5
# b = int(a)
# print(type(b))
# b = float(a)
# print(type(b))
# b = complex(a)
# print(type(b))
# b = bool(a)
# print(type(b))
# b = str(a)
# print(type(b))

# escaping charrecters
# print("Hello World")
# print("Hello\nWorld")
# print("Hello\tWorld")
# print("Hello World\r123")
# print("Hello\bWorld")
# print("Hello\\World")

# operators

# arthimatic + - * / % // 

# a = 10
# b = 5.5
# c = 6.9
# d = 2
# e = 3

# print(f"Addition (a+d): {a+d}")
# print(f"Subtraction (a-d): {a-d}")
# print(f"Multiplication (a*d): {a*d}")
# print(f"Division (a/d): {a/d}")
# print(f"FloorDivision (a//d): {a//d}")
# print(f"Mod (a%d): {a%d}")
# print(f"Mod (a%e): {a%e}")
# print(f"Expo (a**d): {a**d}")
# import math
# a = 4.6
# b = 4.4
# print(math.ceil(a))
# print(math.ceil(b))
# print(math.floor(a))
# print(math.floor(b))
# print(round(a))
# print(round(b))
# l = [95,42,77,56,89]
# count = 0
# for i in l:
#     if(i > 65):
#         print(i)
#         count = count + 1
# print(count)
# l = [95,42,77,56,89]
# # print(l[::-1])
# a = len(l)
# empty = []
# for i in range(a-1,-1,-1):
#     empty.append(l[i])
# print(empty)

# t = ( 10,10,10,"MOHAN",10)
# print ( 10 in t)
# print(2 ** 3 ** 2)

# print(5 and 0)
# print(0 and 5)
# print(5 or 0)
# print(0 or 5)
# x = 10
# y = 0

# a = [1,2,3]
# b = [1,2,3]
# c = a
# print(a == b)
# print(a is b)
# print(a is c)

# print ( 'a' == 97 )
# print ( "11" == 11 )

# print ( 0 or 1 or False or 9)

# radius = float(input ())
# A = 3.14*(radius**2)
# print(A)

# print( -152 & -127)

# identity operator and membership operator

# print( 10 in [10,20,30,10])
# print ( 30 in [20,80,0,10] )
# print ( "a" in "abcd")
# print ( 20 not in [20,10,30])
# print (4 in range(1,10,2) )

# same value but diffrent object address
# support in list,set,frozenset,dict (50% tuple)
# a = {10}
# a = [10,20]
# print(a)
# print(type(a))
# print(id(a))
# b= {10}
# b = [10,20]
# print(b)
# print(type(b))
# print(id(b))

# same value same object address
# support in int,float,str,bool,complex (50% tuple)

# a = 10
# b = 10
# print(id(a))
# print(id(b))

# tuple 50% place in react

# a = (10,20,30)
# b = (10,20,30)

# print(id(a))
# print(id(b))

# a = (10,20,[1,2])
# b = (10,20,[1,2])

# print(id(a))
# print(id(b))

# Identity Operoter
# a = 10
# b = 20
# c = a
# print ( a is b)
# print ( a is c)
# print ( a is not b)
# a = 2.5
# b = 2.5
# c = a
# print ( a is b)
# print ( a is c)
# print ( a is not b)
# a = "abc"
# b = "ABC"
# c = a
# print ( a is b)
# print ( a is c)
# print ( a is not b)
# a = [10,20]
# b = [10,20]
# c = a
# print ( a is b)
# print ( a is c)
# print ( a is not b)
# a = (1,2,3)
# b = (1,2,3)
# c = a
# print ( a is b)
# print ( a is c)
# print ( a is not b)
# a = "abc"  
# b = "cba"
# c = a
# print ( a is b)
# print ( a is c)
# print ( a is not b)
# print(5 & 4)
# print(65 & 96)

# if statements

# Age = int(input("Enter the Age:"))
# if Age >= 18:
#     print("Eligible For Voting ") 
#     if Age >=25:
#         print("DOnate blood")
#     else: 
#         print("you're Not Eligible Blood Donation")
# else: #Age <18
#     print("not Eligible because youre Minor")   

# num = int(input("Enter a number: "))

# if num > 1:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print("Not a Prime Number")
#             break
#     else:
#         print("Prime Number")
# else:
#     print("Not a Prime Number")

# n = eval ( input ( "Enter a number: "))
# if ( n > 0):
#     print( "Positive Number")
# elif ( 0 > n):
#     print( "Negative Number")
# else:
#     print("Zero")
    
# n = eval ( input( " Enter a Number"))
# if (n%2==0):
#     print("Even")
# else:
#     print("Odd")

# n = []
# for i in range(3):
#     num = eval ( input( " Enter a Number: "))
#     n.append(num)
# l = len (n)
# a = n[0]
# for i in range (1,len(n)):
#     if (n[i] > a):
#         a = n[i]
# print (a)

# import sys
# print (sys.argv[2])
# for  i in sys.argv[2]:
#     print(i)



# amount = int(input( "Enter the price: "))
# d = amount/100
# if amount >= 5000:
#     x = d * 20
#     print ( f"20 % Discount Apllaied : {amount-x}")
# elif amount >= 3000:
#     x = d * 15
#     print ( f"15 % Discount Apllaied : {amount-x}")
# elif amount >= 1000:
#     x = d * 10
#     print ( f"10 % Discount Apllaied : {amount-x}")
# else:
#     print(f"No Discount Apllaied : {amount}")

# a = eval ( input("A value: "))
# b = eval ( input("B value: "))
# print ( f"Sum: {a+b}")

# principal_amt = eval (input("Enter a Amount: "))
# intrest  = eval (input("Enter a intrest: "))
# duration = eval (input("Enter a duration: "))
# if ( 1 <= principal_amt <= 10**7 ):
#     if ( 1 <= intrest <= 100):
#         if ( 1 <= duration <= 100):  
#             si = (principal_amt*intrest*duration)/100
#             print(f"Simple Intrest: {si}")


            

# pi=3.14159
# radius = eval ( input("Radius: "))
# if (0<= radius <= 10**5):
#     area = pi*(radius**2)
#     print(f"Area of Square:{area:.2f}")

# n = eval ( input("Enter A Number: ")) 
# if -10**4 <n < 10**4:
#     square = n*n
#     cube = (n*n)*n
#     print (f"Square = {square}")
#     print (f"Cube = {cube}")


# c = float ( input ("Enter a Celsius: "))
# if -100 <= c <= 100:
#     f = ( c * 9 / 5 ) + 32
#     print (f"Temperature in Fahrenheit = {f:.1f}")

# first = float(input("first value: "))
# second = float(input("second value: "))
# third = float(input("third value: "))
# if -10**5 <= first <= 10**5:
#     if -10**5 <= second <= 10**5:
#         if -10**5 <= third <= 10**5:
#             average = (first+second+third)/3
#             print( f"Average = {average} ")
   
   
# a = eval (input(" Enter A Value: "))         
# b = eval (input("Enter B Value: ")) 
# print ("Before Swap")
# print (f"A value {a}")     
# print (f"B value {b}")    
# a,b=b,a
# print ("After Swap")
# print (f"A value {a}")     
# print (f"B value {b}")     

# dividend = int( input("dividend: ")) 
# divisor = int( input("divisor: " ))
# if -10**6 <= dividend <= 10**6:
#     if divisor == 0:
#         print ( "divisor will not be zero" )
#     elif -10**6 <= divisor <=10**6:
#         print(dividend % divisor)
        
# num = int (input ("Enter a Number: "))
# if -10**6 <= num <= 10**6:
#     if num == 0:
#         print("Zero is not define: ")
#     elif (num%2==0):
#         print("Even")
#     else:
#         print("Odd")

# num = int(input("Enter a number"))
# sum = 0
# for i in str(num):
#     sum = sum + int(i)
# print (sum)


# num = float (input("Enter a Number: "))
# if -10**6 <= num <= 10**6:
#     if num>0:
#         print("Positive")
#     elif num<0:
#         print("Negative")
#     else:
#         print("Zero")
        
# a = eval (input ("Enter a Number: "))
# b = eval (input ("Enter a Number: "))
# if -10**6 <= a <= 10**6:
#     if -10**6 <= b <= 10**6:
#         if (a > b):
#             print (f"{a} is greater")
#         elif (b > a):
#             print (f"{b} is greater")
#         else:
#             print("Both are equal")

# a = eval (input ("Enter a Number: "))
# b = eval (input ("Enter a Number: "))
# c = eval (input ("Enter a Number: "))
# if -10**6 <= a <= 10**6:
#   if -10**6 <= b <= 10**6:
#       if -10**6 <= c <= 10**6:
          
#           if (a > b and a > c):
#               print (f"{a} is greater")
#           elif (b > a and b > c):
#               print (f"{b} is greater")
#           elif (c > a and c > b):
#               print (f"{c} is greater")
#           else:
#               print("All are equal")

# year = int (input("Enter a Year: "))
# if 1 <= year <= 9999:
#     if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#         print("Leap Year")
#     else:
#         print("Not a Leap Year")
# else:
#     print("Enter valid value")

# value = str (input("Enetr a character: "))
# vowel = ["a","e","i","o","u"]
# if (len(value) == 1):
#     if (value.lower() in vowel):
#         print("Vowel")
#     elif (value.lower() not in vowel):
#         print("Consonant")
# else:
#     print("Give a Single Character only!")

# marks = float(input("Enter a mark: "))
# if 1<= marks <=100:
#     if marks >= 40:
#         print("Pass")
#     elif marks < 40:
#         print("Fail")
        
# marks = float(input("Enter a mark: "))
# if 1<= marks <=100:
#     if 90<= marks <=100 :
#         print("Grade: A")
#     elif 80 <= marks <=89 :
#         print("Grade: B")
#     elif 70 <= marks <=79 :
#         print("Grade: C")
#     elif 60 <= marks <=69 :
#         print("Grade: D")
#     elif marks <60 :
#         print("Fail")
    
# units = int(input("Enter a units: "))
# if units <= 0:
#     units = units - (units*2)
#     if 0 <= units <=100 :
#         bill = units * 2
#         print(f"Total Bill= {bill}")
#     elif 100 < units <=200 :
#         bill = units * 3
#         print(f"Total Bill= {bill}")
#     elif 200 < units :
#         bill = units * 5
#         print(f"Total Bill= {bill}")
# else:
#     print("Give Only Negative Number Units")

# number = int ( input("Give a Number: "))
# if -10**6 <= number <= 10**6:
#     if (number % 3 == 0 and number % 5 == 0):
#         print (f"{number} is Divisible by both 3 and 5")
#     else :
#         print (f"{number} is Not Divisible by both 3 and 5")

# user1 = {"Username":"admin","Password":1234}
# Username = "admin"
# Password = 1234
# username = str(input("Enter a Username: "))
# password = int(input("Enter a Password: "))
# if (password == Password and username == Username):
#     print("Login Successful")
# else: 
#     print("Invalid Credentials")

# user1 = {"Username":"admin","Password":1234}
# username = str(input("Enter a Username: "))
# password = int(input("Enter a Password: "))
# if (username == user1["Username"] and password == user1["Password"]):
#     print("Login Successful")
# else: 
#     print("Invalid Credentials")



# sub1 = int (input("Enter a Mark sub1: "))
# sub2 = int (input("Enter a Mark sub2: "))
# sub3 = int (input("Enter a Mark sub3: "))
# attendance = int(input("Enter a attendance %: "))
# project = int (input(" Enter a Project Mark: "))
# average = 0
# if (0 <= sub1 <= 100):
#     if ( sub1 < 35 ):
#         print("fails")
#     else:
#         if (0 <= sub2 <= 100):
#             if ( sub2 < 35 ):
#                 print("fails")
#             else:
#                 if (0 <= sub3 <= 100):
#                     if ( sub3 < 35 ):
#                         print("fails")
#                     else:
#                         if (0 <= attendance <= 100):
#                             if attendance < 65:
#                                     print("Detained for Attendance")
#                             else:
#                                 average = (sub1+sub2+sub3)/3
#                                 if project >= 45:
#                                     average += 5
#                                 elif 35  <= project <= 44:
#                                     average += 3
#                                 else:
#                                     average += 0
# if (average>=85 ):
#     print("Distinction")
# elif ( 70 <= average < 85):
#     print("First Class")
# elif ( 50 <= average < 70):
#     print("Second Class")
# elif( 35 <= average < 50):
#     print("Pass")
# else:
#     print("Fail")


# names = ["Mo", "Kavi", "Raju", "Sam", "Kumar", "Abi"]
# search = "Abi"
# for i in names:
#     if i == search:
#         print("Found: Abi")
#         break
# else:
#     print("Not Found: Abi")

# passwords = ["abc", "hello@", "py thon", "secure"] 

# passwords = ["hello",]

# for i in passwords:
#     if i in " ":
#         print(f"Skipped (space found): {i}")
#         continue
#     elif (len(i) < 6):
#         print(f"Too Short: {i}")
#         continue
#     elif i in "e" :
#         print(f"Strong password:{i}")
#         continue
#     elif len(i) == 6:
#         print(f"Weak Password: {i}")
#         continue
#     else:
#         pass

# num = int (input("Enter a days: "))  
# if num > 0:
#     if num >= 7:
#         week = num // 7
#         day = num % 7
#         print(f"{week} Weeks {day} Days")
#     else:
#         print(f"0 Weeks {num} Days")
    
# num = int(input("Give a Number: "))
# if num > 0:
#     if (num % 7==0):
#         print("Divisible by 7")
#     else:
#         print("Not divisible by 7")

# a = int(input("Enter 'a' value: " ))
# b = int(input("Enter 'b' value: " ))
# if a>0:
#     if b>0:
#         if (a % b == 0):
#             print(f"{a} is a multiple of {b}")
#         else:
#             print(f"{a} is not a multiple of {b}")

# num = input("Enter a value: ")
# nums = [1,2,3,4,5,6,7,8,9,0]
# if (type(num) == str or type(num) == int,float):
#     if (int(num) in nums):
#         num = int(num)
#         if (type(num)==(int or float)):
#             print("Digit")
#     else:
#         if(type(num) == str):
#             if ( num == num.lower()):
#                 print("Lowercase Letter")
#             elif ( num == num.upper()):
#                 print("Uppercase Letter")

# num = input("Enter a value: ")

# if num.isdigit():
#     print("Digit")

# elif num.isalpha():
#     if num.islower():
#         print("Lowercase Letter")
#     elif num.isupper():
#         print("Uppercase Letter")
# else:
#     print("Special Character or Mixed Input")


# a = eval(input("Enter a first NUmber: "))
# b = eval(input("Enter a second Number: "))
# operator = input("Enter the operator: ")
# if -10**6 <= a <= 10**6 and -10**6 <= b <= 10**6:
#         if operator == "+":
#             print(f"Result: {a+b}")
#         elif operator == "-":
#             print(f"Result: {a-b}")
#         elif operator == "*":
#             print(f"Result: {a*b}")
#         elif operator == "/":
#             if b != 0:
#                 print(f"Result: {a/b}")
#             else:
#                 print("zero divisin error!")
#         else:
#             print("Give a Valiad Operator!")

a = -19
b = 127
a = a^b
b = a^b
a = a^b
print(f"Value of A: {a}")
print(f"Value of B: {b}")
