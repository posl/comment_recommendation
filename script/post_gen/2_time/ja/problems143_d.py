Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    L = list(map(int,input().split()))
    L.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if L[i] == L[j] == L[k]:
                    ans += 1
                elif L[i] == L[j]:
                    if L[i] + L[j] > L[k]:
                        ans += 1
                elif L[i] == L[k]:
                    if L[i] + L[k] > L[j]:
                        ans += 1
                elif L[j] == L[k]:
                    if L[j] + L[k] > L[i]:
                        ans += 1
                else:
                    if L[i] + L[j] > L[k]:
                        ans += 1
    print(ans)

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
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] < L[i] + L[j]:
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i] and L[i] + L[j] > L[k]:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    count = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[i] != L[k]:
                    if L[i] + L[j] > L[k]:
                        count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[k] < L[i] + L[j]:
                    count += 1
    print(count)

main()

=======
Suggestion 7

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if l[i] < l[j]+l[k] and l[j] < l[k]+l[i] and l[k] < l[i]+l[j]:
                    count += 1
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    L = [int(x) for x in input().split()]
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if L[i] + L[j] > L[k]:
                    ans += 1
                else:
                    break
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l)
    ans = 0
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                if l[a] == l[b] or l[b] == l[c] or l[c] == l[a]:
                    continue
                if l[a] + l[b] > l[c]:
                    ans += 1
    print(ans)
