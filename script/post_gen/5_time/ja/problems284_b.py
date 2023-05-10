Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        count = 0
        for j in range(N):
            if A[j] % 2 != 0:
                count += 1
        print(count)

=======
Suggestion 2

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        ans = 0
        for j in range(n):
            if a[j] % 2 == 1:
                ans += 1
        print(ans)

=======
Suggestion 3

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(len([i for i in a if i%2 == 1]))

=======
Suggestion 4

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        count = 0
        for j in range(n):
            if a[j] % 2 == 1:
                count += 1
        print(count)

=======
Suggestion 5

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        odd = 0
        for j in range(n):
            if a[j] % 2 == 1:
                odd += 1
        print(odd)

=======
Suggestion 6

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(len([a for a in A if a % 2 == 1]))

=======
Suggestion 7

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        odd = 0
        for j in a:
            if j % 2 == 1:
                odd += 1
        print(odd)

=======
Suggestion 8

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        cnt = 0
        for i in range(n):
            if a[i] % 2 == 1:
                cnt += 1
        print(cnt)

=======
Suggestion 9

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    count = 0
    for i in range(n):
        if a[i] % 2 == 1:
            count += 1
    print(count)
