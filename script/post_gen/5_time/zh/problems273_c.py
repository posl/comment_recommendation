Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * n
    for i in range(n - 1):
        if a[i] < a[i + 1]:
            ans[i + 1] = ans[i] + 1
        else:
            ans[i + 1] = ans[i]
    for i in range(n):
        print(ans[i])

=======
Suggestion 2

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int,input().split()))

    A.sort()
    #print(A)

    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])

    for K in range(N):
        #print(K)
        #print(A[K])
        #print(A[K+1])
        #print(A[K+2])
        #print(A[K+3])
        #print(A[K+4])
        #print(A[K+5])
        #print(A[K+6])
        #print(A[K+7])
        #print(A[K+8])
        #print(A[K+9])
        #print(A[K+10])
        print(len(set(A[K:])))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0]*N
    for i in range(N):
        if i > 0 and A[i] == A[i-1]:
            ans[i] = ans[i-1]
        else:
            ans[i] = i - A[:i].count(A[i])
    for a in ans:
        print(a)

=======
Suggestion 5

def main():
    input()
    A = list(map(int, input().split()))
    A.sort()
    n = len(A)
    ans = [0] * n
    for i in range(n):
        if i > 0 and A[i] == A[i - 1]:
            ans[i] = ans[i - 1]
            continue
        l = 0
        r = n
        while r - l > 1:
            m = (l + r) // 2
            if A[m] > A[i]:
                r = m
            else:
                l = m
        ans[i] = l
    for i in ans:
        print(i)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1
    d = sorted(d.items(), key=lambda x: x[0])
    ans = 0
    for i in range(len(d)):
        if i == 0:
            ans += d[i][1]
            print(ans)
        else:
            ans += d[i][1]
            if d[i][0] == d[i-1][0]:
                print(ans - d[i][1])
            else:
                print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(10**9+1)
    ans = [0] * N
    cnt = 0
    for i in range(N):
        cnt += 1
        if A[i] != A[i+1]:
            ans[cnt-1] += 1
            cnt = 0
    print('\n'.join(map(str, ans)))

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * n
    i = 0
    for j in range(1, n):
        while a[i] < a[j]:
            ans[j] += 1
            i += 1
    for i in ans:
        print(i)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 1
    ans = [0] * n
    for i in range(n):
        if i == 0:
            ans[i] = 1
        else:
            if a[i] == a[i - 1]:
                ans[i] = count
            else:
                count += 1
                ans[i] = count
    for i in range(n):
        print(ans[i])

=======
Suggestion 10

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0] * n
    ans[0] = 0
    for i in range(1, n):
        if A[i] > A[i - 1]:
            ans[i] = ans[i - 1] + 1
        else:
            ans[i] = ans[i - 1]
    for i in range(n):
        print(ans[i])
    return 0
