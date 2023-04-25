Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        for j in range(i, N):
            for k in range(j, N):
                if A[i] + A[j] + A[k] <= W:
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    dp = [0] * (w + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(w, a[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - a[i]])
    ans = 0
    for i in range(w + 1):
        if dp[i]:
            ans += 1
    print(ans)

=======
Suggestion 3

def solve(n, w, a):
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if a[i] + a[j] + a[k] <= w:
                    ans += 1
                else:
                    break
    return ans

=======
Suggestion 4

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    dp = [0] * (W + 1)
    for i in range(N):
        for j in range(W, A[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - A[i]] + A[i])
    print(dp[W])

=======
Suggestion 5

def main():
    import sys
    input = sys.stdin.readline
    n,w = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] > w:
            break
        ans += 1
        for j in range(i+1,n):
            if a[i] + a[j] > w:
                break
            ans += 1
            for k in range(j+1,n):
                if a[i] + a[j] + a[k] > w:
                    break
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    # A[i] + A[j] + A[k] <= W となるような i, j, k の組み合わせの個数を求める
    # 1 <= i <= j <= k <= N としたとき、A[i] + A[j] + A[k] <= W となるとき、
    # A[k] <= W となるような最大の k が存在する。
    # このとき、A[i] + A[j] <= W - A[k] となるような i, j の組み合わせの個数は、
    # A[i] + A[j] <= W - A[k] となるような最大の j が存在する。
    # このとき、A[i] <= W - A[k] - A[j] となるような最大の i が存在する。
    # このとき、A[i] <= W - A[k] - A[j] となるような i の個数は、
    # A[i] <= W - A[k] - A[j] となるような最小の i が存在する。
    # このとき、A[i] >= W - A[k] - A[j] となるような最小の i が存在する。
    # このとき、A[i] >= W - A[k] - A[j] となるような i の個数は、
    # A[i] >= W - A[k] - A[j] となるような最大の i が存在する。
    # このとき、A[i] <= W - A[k] - A[j] となるような i の個数は、
    # A[i] <= W - A[k] - A[j] となるような最大の i が存在する。
    # このとき、A[i] <= W - A[k] - A[j]

=======
Suggestion 7

def solve(N, W, A):
    A.sort()
    A = A[::-1]
    a = A[0]
    b = A[1]
    c = A[2]
    d = A[3]
    e = A[4]
    f = A[5]
    g = A[6]
    ans = 0
    for i in range(W//a+1):
        for j in range((W-i*a)//b+1):
            for k in range((W-i*a-j*b)//c+1):
                for l in range((W-i*a-j*b-k*c)//d+1):
                    for m in range((W-i*a-j*b-k*c-l*d)//e+1):
                        for n in range((W-i*a-j*b-k*c-l*d-m*e)//f+1):
                            for o in range((W-i*a-j*b-k*c-l*d-m*e-n*f)//g+1):
                                if i*a+j*b+k*c+l*d+m*e+n*f+o*g <= W:
                                    ans += 1
    return ans

N, W = map(int, input().split())
A = list(map(int, input().split()))
print(solve(N, W, A))

=======
Suggestion 8

def main():
    # get input
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    
    # initialize
    ans = 0
    for a in range(N):
        for b in range(N):
            for c in range(N):
                for d in range(N):
                    for e in range(N):
                        for f in range(N):
                            for g in range(N):
                                if A[a]+A[b]+A[c]+A[d]+A[e]+A[f]+A[g] <= W:
                                    ans += 1
    print(ans)

main()

=======
Suggestion 9

def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))

    # Aの要素を0からWまでの範囲に収める
    B = [0] * (W + 1)
    for i in range(N):
        B[A[i]] += 1

    # Bの要素の累積和を取る
    C = [0] * (W + 1)
    for i in range(1, W + 1):
        C[i] = C[i - 1] + B[i]

    # 答えを求める
    ans = 0
    for i in range(W + 1):
        for j in range(i + 1):
            for k in range(j + 1):
                if i + j + k <= W:
                    ans += C[i] * C[j] * C[k]

    print(ans)
