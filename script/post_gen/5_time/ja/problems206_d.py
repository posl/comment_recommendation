Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N//2):
        if A[i] != A[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a_set = set(a)
    if len(a_set) == 1:
        print(0)
        exit()
    
    a.sort()
    ans = 0
    for i in range(n//2):
        if a[i] != a[n-1-i]:
            ans += 1

    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n//2):
        if a[i] != a[n-1-i]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n//2):
        if a[i] != a[-(i+1)]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    i = 0
    j = n - 1
    while i < j:
        if a[i] == a[i + 1]:
            i += 2
        else:
            i += 1
        if a[j] == a[j - 1]:
            j -= 2
        else:
            j -= 1
        ans += 1
    if i == j:
        ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N//2):
        if A[i] != A[N-1-i]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    #print(N, A)
    A.sort()
    #print(N, A)
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            #print(A[i], A[j])
            if A[i] != A[j]:
                cnt += 1
            else:
                break
    print(cnt)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*(2*10**5+1)
    ans = 0
    for i in range(n):
        b[a[i]] += 1
    for i in range(2*10**5):
        if b[i] > 1:
            ans += b[i] - 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A = sorted(A)
    ans = 0
    i = 0
    j = N-1
    while i < j:
        if A[i] == A[j]:
            i += 1
            j -= 1
        else:
            ans += 1
            if A[i] < A[j]:
                i += 1
                A[i] += A[i-1]
            else:
                j -= 1
                A[j] += A[j+1]
    print(ans)
