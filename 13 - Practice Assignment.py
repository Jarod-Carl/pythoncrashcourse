# Be sure you went through each of the scripts and understood most of what you encountered, because you'll need several of the skills that you aquired to solve this assignment.


# your goal:
# add code to the function below.
# The code has a parameter called num
# The goal of the function is to return a list with every EVEN number from 0 until one less than num.


# ---------------------------------------------------------------------------------- #
def even_numbers(num):
    # num is a positive integer greater than zero
    # return a list of all even integers from 0 until 1 less than the number
    # For example, if the number is 6, return [0,2,4]

    # write your code here    
    
    # replace the return value your even number list
    return []


# ---------------------------------------------------------------------------------- #



# DO NOT CHANGE ANY CODE BELOW HERE

# When you are ready to test your fuction, save your code and run the script. The output will show if you passed or failed each of the tests.
# Your goal is to pass all of the tests.





# ---------------------------------------------------------------------------------- #

# These are test cases which will run against your code
cases = [2, 5, 20, 41, 50, 71]
# Wow, you can put lists inside of lists? That's pretty cool!
answers = [
    [0],
    [0, 2, 4],
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18],
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48],
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70]
]

# This will run the test cases and see if the correct answer is found.

for i in range(len(cases)):
    current_case = cases[i]
    current_answer = answers[i]
    user_answer = even_numbers(current_case)
    if (current_answer == user_answer):
        print("Test",i+1,"PASSED.")
    else:
        print("Test",i+1,"FAILED. Case:",current_case,"Target Answer:",current_answer,"Your answer:",user_answer)

    



