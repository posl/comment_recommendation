Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    d = [0] * k
    a = [0] * k
    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int, input().split()))
    # print(n, k, d, a)

    # すぬけ君のリストを作る
    snuke = [0] * n
    for i in range(k):
        for j in range(d[i]):
            snuke[a[i][j] - 1] += 1
    # print(snuke)

    # お菓子を持っていないすぬけ君を数える
    count = 0
    for i in range(n):
        if snuke[i] == 0:
            count += 1
    # print(count)

    print(count)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        if i+1 not in sum(A, []):
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = [0] * K
    for i in range(K):
        d = int(input())
        A[i] = list(map(int, input().split()))
    A = sum(A, [])
    print(N - len(set(A)))

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    d = []
    A = []
    for i in range(K):
        d.append(int(input()))
        A.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(K):
            if i+1 in A[j]:
                break
        else:
            ans += 1
    print(ans)
    return 0

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    d = []
    a = []
    for _ in range(k):
        d.append(int(input()))
        a.append(list(map(int, input().split())))
    s = set()
    for i in range(k):
        for j in range(d[i]):
            s.add(a[i][j])
    print(n - len(s))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = []
    for i in range(K):
        d = int(input())
        A.append(list(map(int, input().split())))
    A = sum(A, [])
    cnt = 0
    for i in range(1, N+1):
        if i not in A:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    d_list = [0] * n

    for _ in range(k):
        d = int(input())
        a_list = list(map(int, input().split()))
        for a in a_list:
            d_list[a - 1] += 1

    print(d_list.count(0))

=======
Suggestion 8

def main():
    # 標準入力の取得
    n, k = map(int, input().split())
    d = [0] * k
    a = [[] for _ in range(k)]
    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int, input().split()))

    # すぬけ君のお菓子の数を格納するリスト
    s = [0] * n
    for i in range(k):
        for j in range(d[i]):
            s[a[i][j]-1] += 1

    # お菓子を持っていないすぬけ君の数を数える
    count = 0
    for i in range(n):
        if s[i] == 0:
            count += 1

    # 結果の出力
    print(count)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = []
    for i in range(K):
        d = int(input())
        A.append(list(map(int, input().split())))
    A = [item for sublist in A for item in sublist]
    A = list(set(A))
    print(N - len(A))

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    A = []
    for i in range(K):
        A.append(list(map(int, input().split())))
    print(N - len(set([A[i][j] for i in range(K) for j in range(1, len(A[i]))])))
