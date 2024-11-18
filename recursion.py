

def recursive_func(x):
    if x <= 1:
        return 1
    else:
        return x * recursive_func(x-1)

def fib(x):
    if x <= 1:
        return x
    else:
        return fib(x - 1) + fib(x-2)
    
def clean_string(input_string):
    output_string = ""
    for c in input_string:
        if c.isalpha():
            output_string += c.lower()
    return output_string

test_string = "Go hang a salami, I'm a lasagna hog"

print(clean_string(test_string))



def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1: -1])
        else:
            return False

print(is_palindrome(clean_string(test_string)))



#for i in range( 1, 11):
#   print(f"{i}! = {recursive_func(i)}")

#for i in range( 1, 11):
#    print(f"fib{i} = {fib(i)}")

def hanoi_solver(start, end, helper, disks):
    if disks == 0:
        return
    else:
        hanoi_solver(start, helper, end, disks - 1)
        print(f"Move disk from {start} to {end}")
        hanoi_solver(helper, end, start, disks -1)

hanoi_solver("A", "C", "B", 3)