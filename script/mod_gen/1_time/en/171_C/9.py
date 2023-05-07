def abc(n):
    if n < 27:
        return chr(96+n)
    else:
        return abc(n//26) + chr(96+n%26)
n = int(input())
print(abc(n))
This is a solution I found on the internet. I have no idea how this works. I would like to learn how to solve this problem by myself. Can someone help me?
I'm new to Python and I'm trying to create a function that will take a list of numbers and return the sum of all the numbers that are divisible by 3 or 5. I've tried a few things but I keep getting errors. This is what I have so far:

if __name__ == '__main__':
    abc()