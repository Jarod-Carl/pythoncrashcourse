# We can use several operators to compare two things

# let's start with 3 variables
x = 10
y = 10
z = 11

# equality operator: ==
# The double equals sign compares two things and returns True if they are equal false if they are not equal
print("1. ",x,"==",y, x==y)
print("2. ",x,"==",z, x==z)

# not equal operator: !=
# The not equal operator compares two things and returns True only if they are NOT equal
print("3. ",x,"!=",y, x!=y)
print("4. ",x,"!=",z, x!=z)

# greater than operator: >
# The greater than operator compares two things and returns True if the value on the left is greater than the value on the right
print("5. ",x,">",y, x>y)
print("6. ",z,">",x, z>x)

# less than operator: < 
# The inverse of the previous operator
print("7. ",x,"<",y, x<y)
print("8. ",y,"<",z, y<z)

# greater than or equal to operator: >=
# Returns True if the value on the left is greater than or equal to the value on the right
print("9. ",x,">=",y, x>=y)
print("10. ",y,">=",z, y>=z)

# less than or equal to operator: <=
# The inverse of the previous operator 
print("11. ",x,"<=",y, x<=y)
print("12.",y,"<=",z, y<=z)


# BREAK IT
# What happens if instead of writing x==z, we write x=z? What happens to x?
# Remember the difference between the functionality of = vs. ==

# sets the value of x to the value of z