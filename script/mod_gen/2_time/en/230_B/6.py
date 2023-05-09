def isSubString(S):
    T = "oxx" * 10**5
    if S in T:
        return "Yes"
    else:
        return "No"
S = input()
print(isSubString(S))
I am a beginner in python, and I am trying to write a code that will print the first 100 prime numbers. I have written the code below, but I am getting the following error message:
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/PrimeNumbers.py", line 13, in <module>
    print(prime(100))
  File "C:/Users/HP/Desktop/PrimeNumbers.py", line 8, in prime
    if n%i == 0:
TypeError: not all arguments converted during string formatting
I don't know how to fix it. Please help.

if __name__ == '__main__':
    isSubString()