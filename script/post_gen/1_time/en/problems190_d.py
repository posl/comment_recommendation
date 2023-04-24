Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        if (N - i) % i == 0:
            ans += 1
        if (N - i) % (i + 1) == 0:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        if (N - i) % i == 0:
            ans += 1
    print(ans*2-1)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            ans += 1
            if i != N // i:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    ans = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ans += 1
            if i != n // i:
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        if N%i==0:
            if i%2==1:
                ans += 1
            if N//i%2==1:
                ans += 1
    if N**0.5%1==0:
        ans -= 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if N % i == 0:
            ans += 1
    print(ans)

=======
Suggestion 7

def   solve ( n ): 
     ans   =   0 
     for   i   in   range ( 1 ,   n   +   1 ): 
         if   n   %   i   ==   0 : 
             ans   +=   1 
     return   ans

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            ans += 2
        if N%i == i:
            ans -= 1
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    result = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if n // i == i:
                result += 1
            else:
                result += 2
    print(result)
