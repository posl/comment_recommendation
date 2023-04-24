Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = "oxx" * 10**5
    if S in T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    T = 'oxx' * 10**5
    if S in T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    S = input()
    T = 'o'*10**5 + 'x'*10**5 + 'o'*10**5
    for i in range(len(T)-len(S)+1):
        if T[i:i+len(S)] == S:
            print('Yes')
            break
    else:
        print('No')

=======
Suggestion 4

def is_substring_of_t(s):
    t = "oxx" * 10**5
    if s in t:
        return "Yes"
    else:
        return "No"

s = input()
print(is_substring_of_t(s))

=======
Suggestion 5

def is_substring(string, substring):
    for i in range(len(string)):
        if string[i] == substring[0]:
            if string[i:i+len(substring)] == substring:
                return True
    return False

=======
Suggestion 6

def is_substring(S: str) -> str:
    T = 'oxx' * 10**5
    if S in T:
        return 'Yes'
    else:
        return 'No'

=======
Suggestion 7

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

=======
Suggestion 8

def main():
    s =
