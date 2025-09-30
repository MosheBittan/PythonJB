##01| Python Basics##
#1
print("output of 2+6 = " , 2+6)
print("output of 6-2 = " , 6-2)
print("output of 6*2 = " , 6*2)

#2
print("output of 6/2 = " , 6/2)
print("output of 6//2 = " , 6//2)
print("output of 6%2 = " , 6%2)

#3
print("output of 5/2 = " , 5/2)
print("output of 5//2 = " , 5//2)
print("output of 5%2 = " , 5%2)

#4 - take input from user a,b and return c=a+b , d=a-b , e=a*b , f=a/b
#you have to convert the string to integer
a=int(input("enter two values for a:"))
b=int(input("enter two values for b:"))
c=a+b
d=(a-b) 
e=a*b
f=a/b

#5 - calculate and print
print("+---------+---------+---------+---------+---------+---------+")
print("|    a    |    b    |  c=a+b  |  d=a-b  |  e=a*b  |  f=a/b  |")
print("+---------+---------+---------+---------+---------+---------+")
# table row (with max 5 decimals, removing trailing zeros when possible)
print(f"| {a:<7.5g} | {b:<7.5g} | {c:<7.5g} | {d:<7.5g} | {e:<7.5g} | {f:<7.5g} |")

print("+---------+---------+---------+---------+---------+---------+")


#6-print
c=a+b
print(f"a+b= {c}")
c=a-b
print(f"a-b= {c}")
c=a*b
print(f"a*b= {c}")
c=a/b
print(f"a/b= {c}")


#7 - take 3 numbers from user and print the sum (1 variable)
a=0
for num in range(3):
    a=a+int(input(f"Task 7 - Enter number {num+1}:"))

print(f"sum of numbers : {a}")


#8 - take 3 numbers from user and print the sum (1 variable)
a=0
for num in range(3):
    a=a+int(input(f"Task 7 - Enter number {num+1}:"))

print(f"sum of numbers : {a}")

#9 - calculate sum of 5 numbers from 2 variable get from users
a=0
b=0
for num in range(5):
    a=int(input(f"Task9 - Enter number {num+1} : "))
    b=b+a
print(f"sum of 5 numbers : {b}")


#10 - (a+b-c)*d/e
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))
d=int(input("Enter the number: "))
e=int(input("Enter the number: "))
if e != 0 :
    print(f"{(a+b-c)*d/e}")
else:
    print("Can't divide in ZERO!!!")


#11 - (a+b-c)*d/e  - 2 VARIABLES
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
a=a+b
b=int(input("Enter the number: "))
a=a-b
b=int(input("Enter the number: "))
a=a*b
b=int(input("Enter the number: "))
if b != 0 :
    a=a/b
    print(f"(a+b-c)*d/e = {a}")
else:
    print("Can't divide in ZERO!!!")


#12/13-square of number

num=int(input("Enter the number "))
print(f"The square of the number {num} is : {num*num}")



#14-Program that get 3 input from user and give square of them in table
var_list = []

for x in range(3):
    num=int(input("Enter number: "))
    var_list.append(num)

print("X     | X*X ")
for i in range(len(var_list)):
    print(f"-------------")
    print(f"{var_list[i]:<5.5g} | {var_list[i]*var_list[i]:<5.5g}")

#15-Triangle space
a=int(input("Please enter one triangle part a : "))
b=int(input("Please enter one triangle part b : "))

print(f"The surface is : {a*b/2}")

#16-the tax of product 17%
a=int(input("What cost of the product? "))
print(f"The tax is :{a*17/100}")

#17-the item without tax and give you full price ( Y=100*UserInput/83   y=final price answer)
x=int(input(r"Enter please price of the item after TAX 17%  discount : "))
print(f"The price with 17% is : {100*x/83}")

#18-User give a product price and give you Tax 17% and Pure price of item
productPrice=int(input("The item price is: "))
tax=productPrice*17/100
priceWithoutTax=productPrice-tax
print(f"The tax price is: {tax} , the pure item price is: {priceWithoutTax}")



#19-User give a product price and give you Tax 17% and Pure price of item
productPrice=int(input("The item price is: "))
print(f"The tax price is: {productPrice*17/100} , the pure item price is: {productPrice-(productPrice*17/100)}")


#20-Student do 5 Exams , Take 5 grades and calculate the average
sum=0
examCounter=5
for grade in range(examCounter):
    sum=sum+int(input(f"What is exam grade {grade+1} ?"))
print(f"Exams average are : {sum/examCounter}")


#21-Calculate from payment the salary of the employer
name=input("Enter the name : ")
payment=int(input("Enter the monthly pay: "))
bonus=int(input("Enter the sum of additions: "))
print(f"{name} salary is : {payment*0.9+bonus}")

#22-take the 4 papers in different colors and prices and calculate the pay for quantity user take
dict_list ={"blue":120,"green":100,"yellow":80,"red":75}

sum=0
for key,value in dict_list.items():
    sum=sum+int(input(f"How much want from {key} ?"))*value

print(f"The sum of all items are: {sum}")


#23 - write program solve this : a1x+b1y=c1 , a2x+b2y=c2 , solve equations square
dict_num={}

for x in ["a1","b1","c1","a2","b2","c2"]:
    dict_num[x] =int(input(f"Enter the value for {x} :"))

print(f"{dict_num}")
#X=(c1*b2-c2*b1)/(a1*b2-a2*b1)
x=(dict_num["c1"]*dict_num["b2"]-dict_num["c2"]*dict_num["b1"])/(dict_num["a1"]*dict_num["b2"]-dict_num["a2"]*dict_num["b1"])
print(f"the x value: {x}")

#Y=(a1*c2-a2*c1)/(a1*b2-a2*b1)
y=(dict_num["a1"]*dict_num["c2"]-dict_num["a2"]*dict_num["c1"])/(dict_num["a1"]*dict_num["b2"]-dict_num["a2"]*dict_num["b1"])
print(f"the y value: {y}")



#23-improve like they do 
print("This progeam solves a system of two linear equations")
a1,b1,c1 =map(int,input("Enter the coeffitients of the first equation (a1, b1, c1):").split())
a2,b2,c2 =map(int,input("Enter the coeffitients of the second equation (a2, b2, c2):").split())
x=(c1*b2-c2*b1)/(a1*b2-a2*b1)
y=(a1*c2-a2*c1)/(a1*b2-a2*b1)

print(f"The solution is: x={x}, y={y}")
