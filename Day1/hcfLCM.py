# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
 
# HCF = 1
 
# for i in range(2,a+1): # for loop
#     if(a%i==0 and b%i==0):
#         HCF = i

# LCM = (a*b)//HCF # integer divison
 
# print("First Number is: ",a)
# print("Second Number is: ",b)
# print("HCF of the numbers is: ",HCF)
# print("LCM of the numbers is:", LCM)
a = int((input("first no:")))
b = int(input("second no:"))
# if a>b:
#     print(a, "is greater")
# elif b>a:
#     print(b, "is greater")
# else:
#     print("equal")

hcf = 1
if (a<=b):
    small = a
else:
    small = b

for i in range(2,small+1): #returns a range of no betn 2 to (great+1)-1 
# eg.range(2,5)=[2,3,4]
    if((a%i)==0 and(b%i)==0):
       hcf = i
print("hcf:",hcf)

lcm = (a*b)//hcf

print("lcm = ",lcm)

