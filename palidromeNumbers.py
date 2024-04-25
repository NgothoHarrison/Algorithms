'''Given an integer x, return true if x is a palindrome, and false otherwise.
    An integer is a palindrome when it reads the same backward as forward.

 '''

def isPalidrome(x):
    if x < 0:
        return False
    else:
        return str(x) == str(x)[::-1] 
    
print(isPalidrome(121)) # True
print(isPalidrome(-121)) # False
print(isPalidrome(10)) # False
print(isPalidrome(-101)) # False