Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i] and L[i] + L[j] > L[k]:
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[k] != l[i]:
                    if l[i] + l[j] > l[k]:
                        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] < L[j] + L[k]:
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] < L[j] + L[k]:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if l[i] + l[j] > l[k]:
                    ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    L = [int(x) for x in input().split()]
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i] and L[i] + L[j] > L[k]:
                    ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    cnt = 0

    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] < L[i] + L[j]:
                    cnt += 1

    print(cnt)

=======
Suggestion 8

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()

    cnt = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if l[i] != l[j] and l[j] != l[k] and l[k] != l[i] and l[i] + l[j] > l[k]:
                    cnt += 1
    print(cnt)

=======
Suggestion 9

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    ans = 0
    for i in range(0, N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] < L[j] + L[k]:
                    ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    L = [int(x) for x in input().split()]
    L.sort(reverse=True)
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if L[i] < L[j] + L[k]:
                    count += 1
    print(count)
