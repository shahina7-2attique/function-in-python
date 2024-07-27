# Python program to find the largest number
# among the  three numbers using library function
a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
c=int(input("enter 3rd number: "))

def maximum(a, b, c):
    list = [a, b, c]
    return max(list)


print(maximum(a, b, c))