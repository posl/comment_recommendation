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
    l.sort(reverse=True)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] < l[j] + l[k]:
                    ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    ans += 1
                else:
                    break
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] < L[i] + L[j]:
                    count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    L = sorted(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] + L[j] > L[k]:
                    ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    L = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] + L[j] > L[k] and L[j] + L[k] > L[i] and L[k] + L[i] > L[j]:
                    ans += 1

    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if l[i] == l[j] or l[j] == l[k] or l[k] == l[i]:
                    continue
                if l[i] + l[j] > l[k]:
                    ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    L = list(map(int,input().split()))
    L.sort()
    cnt = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if L[i] != L[j] and L[j] != L[k] and L[k] < L[i] + L[j]:
                    cnt += 1
    print(cnt)

=======
Suggestion 9

def main():
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if l[i] + l[j] > l[k]:
                    ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    l = sorted(list(map(int, input().split())))
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    count += 1
    print(count)
