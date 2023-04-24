Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i] and L[i] + L[j] > L[k]:
                    ans += 1
    print(ans)
    return 0

=======
Suggestion 2

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] + L[j] > L[k]:
                    ans += 1
    print(ans)

=======
Suggestion 3

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
Suggestion 4

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
Suggestion 5

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    cnt = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if L[i] + L[j] > L[k]:
                    cnt += 1
                else:
                    break
    print(cnt)

=======
Suggestion 6

def main():
    N = int(input())
    L = sorted(list(map(int, input().split())))
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] < L[i] + L[j]:
                    count += 1
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    L = [int(i) for i in input().split()]
    L.sort()
    cnt = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] + L[j] > L[k]:
                    cnt += 1
                else:
                    break
    print(cnt)

main()

=======
Suggestion 8

def main():
    N = int(input())
    L = [int(x) for x in input().split()]
    L.sort()
    count = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if L[i] < L[j] + L[k]:
                    count += 1
    print(count)

=======
Suggestion 9

def main():
    n = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i] + l[j] > l[k]:
                    count += 1
                else:
                    break
    print(count)

=======
Suggestion 10

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        a = l[i]
        for j in range(i):
            b = l[j]
            for k in range(j):
                c = l[k]
                if a < b + c:
                    ans += 1
    print(ans)
