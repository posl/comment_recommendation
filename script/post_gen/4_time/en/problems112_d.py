Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a%b
    return a

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 4

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    ans = 1
    for i in range(1, int(m**0.5)+1):
        if m % i == 0:
            if m // i >= n:
                ans = max(ans, i)
            if i >= n:
                ans = max(ans, m // i)
    print(ans)

=======
Suggestion 6

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

N, M = map(int, input().split())
ans = 1

for i in range(1, int(M**0.5)+1):
    if M%i == 0:
        if M//i >= N:
            ans = max(ans, i)
        if i >= N:
            ans = max(ans, M//i)
print(ans)

Hi,

I am having trouble with the following problem:

I have a list of numbers, which are in a random order. I need to sort the list in ascending order. I know that the numbers are in the range 1 to 100, so I can use counting sort. I need to use the list index as the key, and the number of occurrences of the number as the value.

My list is as follows:

[19, 21, 24, 21, 19, 18, 19, 21, 19, 21, 19, 18, 19, 18, 19, 19, 18, 18,

=======
Suggestion 7

def gcd(x,y):
    while y:
        x, y = y, x % y
    return x

N,M = map(int,input().split())
ans = 1
for i in range(1,int(M**0.5)+1):
    if M%i == 0:
        if M//i >= N:
            ans = max(ans,i)
        if i >= N:
            ans = max(ans,M//i)
print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    print(M // N)

=======
Suggestion 9

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a
