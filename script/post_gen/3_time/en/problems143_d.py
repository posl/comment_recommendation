Synthesizing 10/10 solutions (Duplicates hidden)

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
                if L[i] + L[j] > L[k]:
                    ans += 1
                else:
                    break
    print(ans)

main()

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
                else:
                    break
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
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if l[i] < l[j] + l[k]:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort(reverse=True)
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if L[i] < L[j] + L[k]:
                    ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    l = sorted(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] != l[j] != l[k]:
                    if l[i] + l[j] > l[k]:
                        ans += 1

    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    l = list(map(int,input().split()))
    l.sort(reverse=True)
    ans = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if l[i] < l[j] + l[k]:
                    ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    l = [int(i) for i in input().split()]
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
Suggestion 9

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    cnt = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if l[i] < l[j] + l[k]:
                    cnt += 1
                else:
                    break
    print(cnt)
