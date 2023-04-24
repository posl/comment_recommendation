Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(N-K+1):
        print(sorted(P[i:i+K])[-1])

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    ans = []
    for i in range(N-K+1):
        ans.append(sorted(P[i:i+K])[-1])
    print(*ans, sep="\n")

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(K, N+1):
        print(sorted(P[:i])[K-1])

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(K, N+1):
        print(sorted(P[:i])[K-1])

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(K, N):
        print(sorted(P[:i])[-K])

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = []
    for i in range(k, n+1):
        ans.append(max(p[i-k:i]))
    for i in ans:
        print(i)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(1, N):
        P[i] += P[i-1]
    ans = 0
    for i in range(K-1, N):
        if i == K-1:
            ans = max(ans, P[i])
        else:
            ans = max(ans, P[i] - P[i-K])
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.insert(0, 0)
    l = [0] * (n + 1)
    for i in range(1, n + 1):
        l[i] = l[i - 1] + p[i]
    for i in range(k, n + 1):
        print(l[i] - l[i - k])

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    # Pの先頭K個の最大値を求める
    max_list = [max(P[:K])]

    # Pの先頭K個の最大値を除いた残りのリストを作る
    for i in range(N-K):
        P.pop(0)
        max_list.append(max(P[:K]))

    # 結果を表示
    for max_val in max_list:
        print(max_val)

=======
Suggestion 10

def get_kth_value(arr, k):
    arr.sort(reverse=True)
    return arr[k-1]
