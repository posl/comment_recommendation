Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * N
    for i in range(N):
        ans[i] = K // N
        if i < K % N:
            ans[i] += 1
    for i in range(N):
        ans[i] += K // N * (a[i] - 1)
        if a[i] <= K % N:
            ans[i] += 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if k <= n:
        for i in range(n):
            print(k)
        return
    else:
        k -= n
        for i in range(n):
            if a[i] <= k // n + ((k % n) > i):
                print(a[i] + k // n + ((k % n) > i))
            else:
                print(a[i])
        return

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * N
    for i in range(N):
        ans[i] += (K // N)
    K %= N
    for i in range(K):
        ans[i] += 1
    for i in range(N):
        print(ans[bisect_left(a, i + 1) - 1])

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = [0] + a
    ans = [0] * (N+1)
    for i in range(1, N+1):
        if K >= i:
            ans[i] = K // i
            K -= ans[i] * i
        else:
            ans[i] = 0
    for i in range(1, N+1):
        if K > 0:
            if a[i] <= K:
                ans[i] += 1
                K -= 1
            else:
                break
    for i in range(1, N+1):
        print(ans[i])

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0]*N
    for i in range(N):
        ans[i] += (K//(N-i))
        if i < K%(N-i):
            ans[i] += 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(10**9+1)
    ans = [0]*N
    cnt = 0
    for i in range(N):
        if i == N-1:
            ans[i] += K
        else:
            cnt += (A[i+1]-A[i])*(i+1)
            if cnt > K:
                ans[i] += K-(cnt-(A[i+1]-A[i])*(i+1))
                cnt = K
            else:
                ans[i] += A[i+1]-A[i]
    for i in range(N):
        print(ans[i])

main()

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))

    # 1. 1 <= N <= 2 * 10^5
    # 2. 1 <= K <= 10^18
    # 3. 1 <= a_i <= 10^9
    # 4. All a_i are pairwise different.
    # 5. All values in input are integers.

    # 1. 1 <= N <= 2 * 10^5
    # 2. 1 <= K <= 10^18
    # 3. 1 <= a_i <= 10^9
    # 4. All a_i are pairwise different.
    # 5. All values in input are integers.

    # 1. 1 <= N <= 2 * 10^5
    # 2. 1 <= K <= 10^18
    # 3. 1 <= a_i <= 10^9
    # 4. All a_i are pairwise different.
    # 5. All values in input are integers.

    # 1. 1 <= N <= 2 * 10^5
    # 2. 1 <= K <= 10^18
    # 3. 1 <= a_i <= 10^9
    # 4. All a_i are pairwise different.
    # 5. All values in input are integers.

    # 1. 1 <= N <= 2 * 10^5
    # 2. 1 <= K <= 10^18
    # 3. 1 <= a_i <= 10^9
    # 4. All a_i are pairwise different.
    # 5. All values in input are integers.

    # 1. 1 <= N <= 2 * 10^5
    # 2. 1 <= K <= 10^18
    # 3. 1 <= a_i <= 10^9
    # 4. All a_i are pairwise different.
    # 5. All values in input are integers.

    # 1. 1 <= N <= 2 * 10^5
    # 2. 1 <= K <= 10^18
    # 3

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(N, K)
    #print(A)
    #print(A[0])
    a = 0
    b = 0
    for i in range(N):
        if A[i] > K:
            b = i
            break
        else:
            a = i
    #print(a, b)
    if a == N-1:
        for i in range(N):
            print(K)
    else:
        for i in range(N):
            if i < b:
                print(K//N)
            elif i == b:
                print(K//N + K%N)
            else:
                print(0)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    # 1人目を0とすると、2人目は1個目のIDを引いた値となる
    # 3人目は2人目のIDを引いた値となる
    # つまり、N人目までのIDを引いた値の合計がK個のお菓子の分配数となる
    # これをN人目までのIDの合計とKを比較し、N人目までのIDの合計がKを超える場合は
    # 1人目から順にK/N個ずつ配る
    # それ以外の場合は、N人目までのIDの合計がKを超えない場合は
    # 1人目から順にIDの値が小さい人からK/N個ずつ配る
    # この場合、N人目のIDの値がK/N+1となる
    # 1人目から順にIDの値が小さい人からK/N個ずつ配る場合は
    # 1人目から順にIDの値が小さい人からK/N個ずつ配る
    # この場合、N人目のIDの値がK/N+1となる
    # 1人目から順にIDの値が小さい人からK/N個ずつ配る場合は
    # 1人目から順にIDの値が小さい人からK/N個ずつ配る
    # この場合、N人目のIDの値がK/N+1となる
    # 1人目から順にIDの値が小さい人からK/N個ずつ配る場合は
    # 1人目から順にIDの値が小さい人からK/N個ずつ

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    # 1. 1~N人までの人数で分けて、その人数で分けられる全てのケースの個数を求める
    # 2. 1~N人までの人数で分けて、その人数で分けられる全てのケースの個数を求める
    # 3. 1~N人までの人数で分けて、その人数で分けられる全てのケースの個数を求める
    # 4. 1~N人までの人数で分けて、その人数で分けられる全てのケースの個数を求める
    # 5. 1~N人までの人数で分けて、その人数で分けられる全てのケースの個数を求める
    # 6. 1~N人までの人数で分けて、その人数で分けられる全てのケースの個数を求める
    # 7. 1~N人までの人数で分けて、その人数で分けられる全てのケースの個数を求める
    # 8. 1~N人までの人数で分けて、その人数で分けられる全てのケースの個数を求める
    # 9. 1~N人までの人数で分けて、その人数で分けられる全てのケースの個数を求める
    # 10. 1~N人までの人数で分けて、その人数で分けられる全てのケースの個数を求める
    # 11. 1~N人までの人数で分けて、その人数で分けられる全て
