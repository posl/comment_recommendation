Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    if K <= N:
        for i in range(N):
            if i < K:
                print(1)
            else:
                print(0)
    else:
        K -= N
        div, mod = divmod(K, N)
        for i in range(N):
            if mod > i:
                print(div + 1)
            else:
                print(div)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * N
    for i in range(N):
        if K >= N:
            ans[i] += 1
            K -= 1
        else:
            ans[i] += K // N
            K -= K // N
    for i in range(N):
        if i < N - K:
            ans[i] += K // (N - i)
        else:
            ans[i] += K // (N - i) + 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0] * N
    for i in range(N):
        if K >= N - i:
            ans[i] = K // (N - i)
            K -= ans[i] * (N - i)
    for i in range(N):
        if K > 0 and A[i] >= ans[i]:
            ans[i] += 1
            K -= 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    ans = [0] * n
    for i in range(n):
        ans[i] = k // n
        if i < k % n:
            ans[i] += 1

    for i in range(n):
        if a[i] <= k:
            ans[i] += k // n
            if i < k % n:
                ans[i] += 1
        else:
            break

    for i in range(n):
        print(ans[i])

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * N
    for i in range(N):
        if K > (N - 1 - i):
            ans[i] += K // (N - i)
            K = K % (N - i)
        else:
            ans[i] += K
            break
    for i in range(N):
        print(ans[i] + (a[i] - 1))

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = [0]*n
    for i in range(n):
        if k >= n-i:
            ans[i] += k//(n-i)
            k %= (n-i)
        else:
            ans[i] += k
            break
    for i in range(n):
        print(ans[i]+a[i]//a[0])

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A + [10**9+1]
    ans = [0] * N
    for i in range(N):
        if A[i+1] - A[i] > 0:
            ans[i] = (A[i+1] - A[i]) * ((i+1) * K // N) - K
            K -= ans[i]
    for i in range(N):
        print(ans[i] // (i+1) + K // N + 1)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    # 国民番号でソート
    A.sort()
    
    # お菓子の配り方の総数
    cnt = K // N
    
    # 1人あたりのお菓子の個数
    for i in range(N):
        if A[i] <= cnt:
            print(cnt)
        else:
            print(K // N + 1)
    
    # 余ったお菓子の配り方
    mod = K % N
    
    # 余ったお菓子の配り方の総数
    cnt = cnt + 1
    
    # 余ったお菓子の配り方で配る人数
    for i in range(mod):
        print(cnt)

main()

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))

    # 配る回数
    count = K // N
    # 配るお菓子の個数
    candy = K % N

    # 回数分配る
    for i in range(N):
        print(count, end="")

        # 配るお菓子の個数が残っている場合
        if candy > 0:
            # 国民番号が小さい順に配る
            if a[i] <= candy:
                print(" " + str(count + 1), end="")
                candy -= a[i]
            else:
                print(" " + str(count), end="")
        else:
            print(" " + str(count), end="")

        print()

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))

    #a_iの値が小さい方からK人を選ぶ
    a.sort()

    #K人選べる回数
    div = K // N
    #余りの人数
    mod = K % N

    for i in range(N):
        if a[i] <= div:
            print(div)
        else:
            if i < mod:
                print(div + 1)
            else:
                print(div)
