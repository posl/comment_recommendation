Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = 0
    for i in str(n):
        s += int(i)
    if n % s == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n = int(input())
    s = 0
    for i in str(n):
        s += int(i)
    if n % s == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    N = int(input())
    S = 0
    for i in str(N):
        S += int(i)
    if N % S == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    n = int(input())
    s = str(n)
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    if n % sum == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

=======
Suggestion 6

def main():
    N = int(input())
    S_N = sum([int(n) for n in str(N)])
    if N % S_N == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def getSumOfDigits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

=======
Suggestion 8

def check(n):
    #print(n)
    #print(sum(list(map(int, str(n)))))
    #print(n % sum(list(map(int, str(n)))))
    if n % sum(list(map(int, str(n)))) == 0:
        print("Yes")
    else:
        print("No")
