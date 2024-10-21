# a conditional statement allows you to run code only if certain conditions are met.

# We use the word "if" to set up a conditional statement.

# For example, let's say we have a list of numbers from 0 to 99:
nums_list = list(range(100))
# This generated a list like this [0,1,2,3...,97,98,99]

# What if we only want to print the numbers divisible by 7?

# We can iterate through the list, and use a conditional to decide if we print the number or not:

for num in nums_list:
    # if the number divides by 7 evenly, it is divisible by 7
    # Do you remember in the data types lesson, we learned about modulo (%)
    # modulo gives us the remainder of a division. If the modulo of two numbers is 0, then the numbers are divisible.
    if num % 7 == 0:
        # notice that inside of the conditional, the print statement is indented once again. This is because the print is inside of the conditional and the conditional is inside of the for loop. If the print weren't indented, the code would not function.
        print(num,"is divisible by 7")


# What if we want to do something if a condition is met and something else if the condition is not met? 
# We can use an if statement along with an else statement.

x = 20
y = 10

if x < y:
    print(x,"is less than",y)
#else:
    # notice the code in else is also indented, indicating it is within the else statement
    print(x,"is not less than",y)

# when we run the code above, it will first check if x (20) is less than y (10).
# Because this is False, it will not run the code within the if statement.
# Instead it will run the code within the else statement.

# BREAK IT:
# What happens if you delete the else statement above (along with the print underneath it)
# Do you get an error?
# Does anything print out?
# Why or why not?

# There isn't an error. The case for else just won't print