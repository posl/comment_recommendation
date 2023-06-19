Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n = int(input())
    c = list(map(int, input().split()))
    return n, c

=======
Suggestion 2

def main():
    N = 2
    C = [1, 3]
    ans = 1
    C.sort()
    for i in range(N):
        ans *= (C[i] - i)
        ans %= (10**9 + 7)
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()

    ans = 1
    for i in range(N):
        ans *= (C[i] - i)
        ans %= (10 ** 9 + 7)
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    c = list(map(int, input().split()))
    ans = 1
    c.sort()
    for i in range(n):
        ans *= max(c[i] - i, 0)
        ans %= 1000000007
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans *= c[i] - i
        ans %= 1000000007
    print(ans)

=======
Suggestion 6

def solve(n,c):
    if n==1:
        return c[0]
    if n==2:
        return (c[0]+c[1])%1000000007
    if n==3:
        return (c[0]+c[1]+c[2])%1000000007
    if n==4:
        return (c[0]+c[1]+c[2]+c[3]+3)%1000000007
    if n==5:
        return (c[0]+c[1]+c[2]+c[3]+c[4]+6)%1000000007
    if n==6:
        return (c[0]+c[1]+c[2]+c[3]+c[4]+c[5]+10)%1000000007
    if n==7:
        return (c[0]+c[1]+c[2]+c[3]+c[4]+c[5]+c[6]+15)%1000000007
    if n==8:
        return (c[0]+c[1]+c[2]+c[3]+c[4]+c[5]+c[6]+c[7]+21)%1000000007
    if n==9:
        return (c[0]+c[1]+c[2]+c[3]+c[4]+c[5]+c[6]+c[7]+c[8]+28)%1000000007
    if n==10:
        return (c[0]+c[1]+c[2]+c[3]+c[4]+c[5]+c[6]+c[7]+c[8]+c[9]+36)%1000000007

n=int(input())
c=list(map(int,input().split()))
print(solve(n,c))

=======
Suggestion 7

def main():
    n = int(input())
    c = list(map(int,input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans *= c[i] - i
        ans %= (10**9 + 7)
    print(ans)

=======
Suggestion 8

def solve():
    n = int(input())
    c = list(map(int, input().split()))
    m = 10 ** 9 + 7
    c.sort()
    ans = 1
    for i in range(n):
        ans *= c[i] - i
        ans %= m
    print(ans)
solve()

=======
Suggestion 9

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans *= max(0, c[i] - i)
        ans %= 1000000007
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    mod = 10**9+7
    ans = 1
    for i in range(n):
        ans *= max(0, c[i]-i)
        ans %= mod
    print(ans)
