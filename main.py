# Take input from the user
# We have to typecast the input as input will return value as string
x = int(input("Enter the value of x:"))
y = int(input("Enter the value of y:"))
z = int(input("Enter the value of z:"))
print("Value of x before swapping:", x)
print("Value of y before swapping", y)
print("Value of z before swapping", z)


# Swapping
temp = x
x = y
y = z
z = temp

print("Value of x after swapping", x)
print("Value of y after swapping", y)
print("Value of z after swapping", z)