Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = ''
    while N > 0:
        N -= 1
        ans = chr(ord('a') + N % 26) + ans
        N //= 26
    print(ans)

main()

=======
Suggestion 2

def main():
    N = int(input())
    ans = ""
    while N > 0:
        N -= 1
        ans = chr(N % 26 + ord('a')) + ans
        N //= 26
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    name = ''
    while n > 0:
        n -= 1
        name = chr(ord('a') + n % 26) + name
        n //= 26
    print(name)

=======
Suggestion 4

def solve():
    N = int(input())
    ans = ""
    while N > 0:
        N -= 1
        ans = chr(ord('a') + N % 26) + ans
        N //= 26
    print(ans)

=======
Suggestion 5

def num_to_name(n):
    if n <= 26:
        return chr(ord('a') + n - 1)
    else:
        return num_to_name((n - 1) // 26) + chr(ord('a') + (n - 1) % 26)

=======
Suggestion 6

def main():
    N = int(input())
    ans = []
    while N > 0:
        N -= 1
        ans.append(chr(N%26 + ord('a')))
        N //= 26
    print(''.join(ans[::-1]))

=======
Suggestion 7

def getDogName(N):
    if N <= 26:
        return chr(ord('a') + N - 1)
    else:
        return getDogName((N - 1) // 26) + getDogName((N - 1) % 26 + 1)

=======
Suggestion 8

def main():
    # put your code here
    n = int(input())
    base = 26
    ans = ''
    while n > 0:
        n -= 1
        ans = chr(n % base + ord('a')) + ans
        n //= base
    print(ans)

=======
Suggestion 9

def getDogName(n):
    n -= 1
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    name = ""
    while n > 25:
        name += alphabet[n % 26]
        n = n // 26 - 1
    name += alphabet[n % 26]
    return name[::-1]

=======
Suggestion 10

def abc(n):
    if n < 27:
        return chr(96+n)
    else:
        return abc(n//26) + chr(96+n%26)

n = int(input())
print(abc(n))

This is a solution I found on the internet. I have no idea how this works. I would like to learn how to solve this problem by myself. Can someone help me?

I'm new to Python and I'm trying to create a function that will take a list of numbers and return the sum of all the numbers that are divisible by 3 or 5. I've tried a few things but I keep getting errors. This is what I have so far:
