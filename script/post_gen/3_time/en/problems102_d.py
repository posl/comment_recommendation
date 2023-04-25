Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    ans = 10 ** 20
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            ans = min(ans, max(S[i], S[j] - S[i], S[N] - S[j]) - min(S[i], S[j] - S[i], S[N] - S[j]))
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    ans = float('inf')
    for i in range(2, N - 1):
        l = 0
        r = N
        while r - l > 1:
            m = (l + r) // 2
            if S[m] < S[i + 1] - S[m]:
                l = m
            else:
                r = m
        ans = min(ans, max(S[l], S[i + 1] - S[l], S[r] - S[i + 1], S[N] - S[r]) - min(S[l], S[i + 1] - S[l], S[r] - S[i + 1], S[N] - S[r]))
        l = 0
        r = N
        while r - l > 1:
            m = (l + r) // 2
            if S[m] < S[i + 1] - S[m]:
                l = m
            else:
                r = m
        ans = min(ans, max(S[l], S[i + 1] - S[l], S[r] - S[i + 1], S[N] - S[r]) - min(S[l], S[i + 1] - S[l], S[r] - S[i + 1], S[N] - S[r]))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    ans = 10 ** 18
    for i in range(N - 2):
        a = S[i + 1]
        b = S[N] - S[i + 1]
        c = abs(a - b)
        ans = min(ans, c)
    for i in range(N - 1):
        a = S[i + 1]
        b = S[N] - S[i + 1]
        c = abs(a - b)
        ans = min(ans, c)
    print(ans)

main()

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 10 ** 9
    for i in range(n - 2):
        ans = min(ans, max(s[i + 1], s[n] - s[i + 1]) - min(s[i + 1], s[n] - s[i + 1]))
    for i in range(n - 1):
        ans = min(ans, max(s[i + 1], s[n] - s[i + 1]) - min(s[i + 1], s[n] - s[i + 1]))
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = [0] * N
    P[0] = A[0]
    for i in range(1, N):
        P[i] = P[i - 1] + A[i]
    Q = [0] * N
    Q[N - 1] = A[N - 1]
    for i in range(N - 2, -1, -1):
        Q[i] = Q[i + 1] + A[i]
    ans = 10 ** 9
    for i in range(1, N - 2):
        for j in range(i + 1, N - 1):
            ans = min(ans, max(P[i - 1], Q[j + 1], P[j - 1] - P[i - 1], P[N - 1] - P[j - 1]) - min(P[i - 1], Q[j + 1], P[j - 1] - P[i - 1], P[N - 1] - P[j - 1]))
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #累積和を求める
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    #print(S)

    #最小値と最大値の差を求める
    def calc(x):
        return max(S[x + 1], S[N] - S[x + 1]) - min(S[x + 1], S[N] - S[x + 1])

    #print(calc(0))
    #print(calc(1))
    #print(calc(2))

    #最小値と最大値の差が最小になる場所を求める
    #最小値と最大値の差が最小になる場所は、最小値と最大値の差を求める際に使った累積和の値が最小になる場所である
    #S[x + 1]が最小になる場所を求める
    #S[x + 1]が最小になる場所は、S[x]が最大になる場所である
    #S[x]が最大になる場所は、S[x]が最大になる場所は、S[x + 1]が最小になる場所である
    #S[x + 1]が最小になる場所は、S[x + 1]が最小になる場所は、S[x]が最大になる場所である
    #S[x + 1]が最小になる場所は、S[x + 1]が最小になる場所は、S[x]が最大になる場所である
    #S[x + 1]が最小になる場所は、S[x + 1]が最小になる場所は、S[x]が最大になる場所である
    #S[x + 1

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = 10 ** 9
    t = 0
    for i in range(n - 1):
        t += a[i]
        ans = min(ans, abs(s - 2 * t))
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i]
    ans = 10**10
    p = 0
    for i in range(n-1):
        p += a[i]
        ans = min(ans, abs(sum - p - p))
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    t = 0
    min_d = 10**18
    for i in range(n-1):
        t += a[i]
        if min_d > abs(s - 2*t):
            min_d = abs(s - 2*t)
    print(min_d)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 10**9
    #AをB,C,D,Eに分ける
    #B = A[:i]
    #C = A[i:j]
    #D = A[j:k]
    #E = A[k:]
    #P,Q,R,S = sum(B),sum(C),sum(D),sum(E)
    #max(P,Q,R,S) - min(P,Q,R,S)の最小値
    #Bの最後の要素はどこか
    #Cの最後の要素はどこか
    #Dの最後の要素はどこか
    #Eの最後の要素はどこか
    #Bの最後の要素はCの最初の要素の直前
    #Cの最後の要素はDの最初の要素の直前
    #Dの最後の要素はEの最初の要素の直前
    #i,j,kはそれぞれB,C,Dの最後の要素の直後のインデックス
    #i = 1
    #j = 2
    #k = 3
    #B = A[:i]
    #C = A[i:j]
    #D = A[j:k]
    #E = A[k:]
    #P,Q,R,S = sum(B),sum(C),sum(D),sum(E)
    #print(P,Q,R,S)
    #print(max(P,Q,R,S) - min(P,Q,R,S))
    #i = 1
    #j = 2
    #k = 4
    #B = A[:i]
    #C = A[i:j]
    #D = A[j:k]
    #E = A[k:]
    #P,Q,R,S = sum(B),sum(C),sum(D),sum(E)
    #print(P,Q,R,S)
    #print(max(P,Q,R,S) - min(P,Q,R,S))
    #i = 1
    #j = 3
    #k = 4
    #B = A[:i]
    #C = A[i:j]
    #D = A[j:k]
    #E = A[k:]
