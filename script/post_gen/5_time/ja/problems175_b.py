Synthesizing 10/10 solutions (Duplicates hidden)

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
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] != l[j] and l[j] != l[k] and l[i] + l[j] > l[k]:
                    ans += 1
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] == L[j] or L[j] == L[k]:
                    continue
                if L[i] + L[j] <= L[k]:
                    break
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
                if l[i] != l[j] and l[j] != l[k] and l[k] != l[i]:
                    if l[i] + l[j] > l[k]:
                        ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[i] + L[j] > L[k]:
                    ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    count = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] == L[j] or L[j] == L[k] or L[k] == L[i]:
                    continue
                if L[k] < L[i] + L[j]:
                    count += 1
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    L = list(map(int,input().split()))
    L.sort()
    cnt = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if L[i] != L[j] and L[j] != L[k] and L[i] + L[j] > L[k]:
                    cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            #print("i, j", i, j)
            for k in range(j+1, n):
                #print("i, j, k", i, j, k)
                if l[i] != l[j] and l[j] != l[k] and l[i] != l[k]:
                    #print("l[i], l[j], l[k]", l[i], l[j], l[k])
                    if l[i] + l[j] > l[k]:
                        ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    L = list(map(int,input().split()))
    L.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i] and L[i] + L[j] > L[k]:
                    ans += 1
    print(ans)
