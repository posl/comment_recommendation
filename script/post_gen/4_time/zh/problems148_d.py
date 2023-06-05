Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] == i+1:
            ans += 1
    if ans == n:
        print(0)
    elif ans == n-1:
        print(1)
    else:
        print(n-ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] != 1:
        print(-1)
        return
    for i in range(1,n):
        if a[i] - a[i-1] > 1:
            print(-1)
            return
    ans = 0
    for i in range(n-1):
        if a[i] + 1 == a[i+1]:
            ans += 1
    print(n-1-ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n)
    #print(a)
    if n == 1:
        print(0)
        return
    if a[0] != 1:
        print(-1)
        return
    a.append(0)
    a.append(0)
    #print(a)
    ans = 0
    for i in range(n):
        if a[i+1] == a[i] + 1:
            ans += 1
        elif a[i+1] > a[i] + 1:
            print(-1)
            return
    print(n - ans)

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] == i + 1:
            ans += 1
    if ans == N:
        print(-1)
    else:
        print(N - ans)

solve()

=======
Suggestion 5

def solve():
    N = int(input())
    a = list(map(int, input().split()))
    #print(N,a)
    #print(len(a))
    if N == 1:
        if a[0] == 1:
            print(0)
        else:
            print(-1)
        exit()
    if N == 2:
        if a[0] == 1 and a[1] == 2:
            print(0)
        elif a[0] == 2 and a[1] == 1:
            print(1)
        else:
            print(-1)
        exit()
    if N == 3:
        if a[0] == 1 and a[1] == 3 and a[2] == 2:
            print(1)
        elif a[0] == 1 and a[1] == 2 and a[2] == 3:
            print(1)
        else:
            print(-1)
        exit()
    if N == 4:
        if a[0] == 1 and a[1] == 2 and a[2] == 4 and a[3] == 3:
            print(1)
        elif a[0] == 1 and a[1] == 3 and a[2] == 4 and a[3] == 2:
            print(1)
        elif a[0] == 1 and a[1] == 2 and a[2] == 3 and a[3] == 4:
            print(2)
        elif a[0] == 1 and a[1] == 4 and a[2] == 3 and a[3] == 2:
            print(2)
        else:
            print(-1)
        exit()
    if N == 5:
        if a[0] == 1 and a[1] == 2 and a[2] == 3 and a[3] == 5 and a[4] == 4:
            print(1)
        elif a[0] == 1 and a[1] == 2 and a[2] == 4 and a[3] == 5 and a[4] == 3:
            print(1)
        elif a[0] == 1 and a[1] == 2

=======
Suggestion 6

def main():
    print("Hello World!")
    N = int(input())
    a = [int(i) for i in input().split()]
    print(N)
    print(a)
    return 0

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] != 1:
        print(-1)
        return
    for i in range(1, n):
        if a[i] - a[i-1] > 1:
            print(-1)
            return
    ans = 0
    for i in range(1, n):
        if a[i] - a[i-1] == 1:
            ans += 1
    print(n - ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] == i + 1:
            ans += 1
    print(-1 if ans == N else N - ans)

main()

=======
Suggestion 10

def main():
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[0]*n
    for i in range(n):
        b[a[i]-1]=i
    ans=0
    for i in range(n-1):
        if b[i]>b[i+1]:
            ans+=1
    print(ans+1)
main()
