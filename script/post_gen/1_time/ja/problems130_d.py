Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    r = 0
    s = 0
    for l in range(n):
        while r < n and s + a[r] < k:
            s += a[r]
            r += 1
        if r == n:
            break
        ans += n - r
        s -= a[l]
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += a[j]
            if s >= k:
                ans += n - j
                break
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        sum = 0
        for j in range(i, N):
            sum += A[j]
            if sum >= K:
                ans += N - j
                break
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    i = 0
    j = 0
    s = 0
    while i < N:
        while j < N and s < K:
            s += A[j]
            j += 1
        if s < K:
            break
        ans += N - j + 1
        s -= A[i]
        i += 1
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    l = 0
    r = 0
    sum = 0
    while l < n:
        if r == n:
            sum -= a[l]
            l += 1
        elif sum < k:
            sum += a[r]
            r += 1
        else:
            sum -= a[l]
            l += 1
        if sum >= k:
            ans += n - r + 1
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    count = 0
    sum = 0
    for i in range(N):
        sum += A[i]
        if sum >= K:
            count += 1
        else:
            ans += count
            count = 0
            sum = 0
    ans += count * (count + 1) // 2
    print(ans)

=======
Suggestion 7

def main():
    # 入力
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    # 累積和
    s = [0]
    for i in range(N):
        s.append(s[i] + a[i])
    # 累積和の差分について、K以上の個数を求める
    ans = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if s[j] - s[i] >= K:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    # Aの連続する部分列の個数はN(N+1)/2
    # つまり、Aの連続する部分列の個数はO(N^2)
    # これを全探索すると、計算量はO(N^3)になる。
    # しかし、Aの連続する部分列の個数はO(N^2)である。
    # つまり、Aの連続する部分列を全探索する計算量はO(N^3)になる。
    # これはTLEになる。
    # そこで、Aの連続する部分列の個数をO(N)に抑える必要がある。
    # つまり、Aの連続する部分列を全探索する計算量をO(N^2)に抑える必要がある。
    # そこで、Aの連続する部分列を全探索する計算量をO(N^2)に抑える。
    # つまり、Aの連続する部分列を全探索する計算量をO(N^2)に抑える。
    # つまり、Aの連続する部分列を全探索する計算量をO(N^2)に抑える。
    # つまり、Aの連続する部分列を全探索する計算量をO(N^2)に抑える。
    # つまり、Aの連続する部分列を全探索する計算量をO(N^2)に抑える。
    # つまり、Aの連続する部分列を全探索する計算量をO(N^2)に抑える。
    # つまり、Aの連続する部分列を全探索する

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    #print(A)
    #print(N,K)
    #print(A)
    #print(A[1:3])
    #print(A[1:3])
    #print(A[2:3])
    #print(A[3:3])
    #print(A[4:3])
    #print(A[5:3])
    #print(A[6:3])
    #print(A[7:3])
    #print(A[8:3])
    #print(A[9:3])
    #print(A[10:3])
    #print(A[11:3])
    #print(A[12:3])
    #print(A[13:3])
    #print(A[14:3])
    #print(A[15:3])
    #print(A[16:3])
    #print(A[17:3])
    #print(A[18:3])
    #print(A[19:3])
    #print(A[20:3])
    #print(A[21:3])
    #print(A[22:3])
    #print(A[23:3])
    #print(A[24:3])
    #print(A[25:3])
    #print(A[26:3])
    #print(A[27:3])
    #print(A[28:3])
    #print(A[29:3])
    #print(A[30:3])
    #print(A[31:3])
    #print(A[32:3])
    #print(A[33:3])
    #print(A[34:3])
    #print(A[35:3])
    #print(A[36:3])
    #print(A[37:3])
    #print(A[38:3])
    #print(A[39:3])
    #print(A[40:3])
    #print(A[41:3])
    #print(A[42:3])
    #print(A[43:3])
    #print(A[44:3])
    #print(A[45:3])
    #print(A[46:3])
    #print(A[47:3])
    #print(A[48:3])
    #print(A[49:3])
    #print(A[50:3])
    #print
