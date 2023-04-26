Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += B.count(A[C[i]-1])
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(N):
            if A[i] == B[C[j]-1]:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(N):
            if A[i] == B[C[j] - 1]:
                count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = [0] * (n + 1)
    for i in c:
        d[i] += 1
    count = 0
    for i in range(n):
        count += d[a[i]] * b[i]
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    a = [0] * (N + 1)
    b = [0] * (N + 1)
    for i in range(N):
        a[A[i]] += 1
        b[B[C[i]]] += 1

    ans = 0
    for i in range(1, N + 1):
        ans += a[i] * b[i]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    #Bの各要素の出現回数をカウント
    B_cnt = [0] * (N+1)
    for b in B:
        B_cnt[b] += 1

    #Cの各要素の出現回数をカウント
    C_cnt = [0] * (N+1)
    for c in C:
        C_cnt[c] += 1

    #Aに対して、Bの各要素の出現回数を掛け合わせる
    ans = 0
    for a in A:
        ans += B_cnt[a] * C_cnt[a]

    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    Bc = [0] * (n + 1)
    for c in C:
        Bc[c] += 1
    Bcsum = [0] * (n + 1)
    for i in range(1, n + 1):
        Bcsum[i] = Bcsum[i - 1] + Bc[i]
    ans = 0
    for a in A:
        ans += Bcsum[B[a - 1]]
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    #Aの各要素の出現回数を数える
    A_count = [0] * (N + 1)
    for i in range(N):
        A_count[A[i]] += 1

    #Bの各要素の出現回数を数える
    B_count = [0] * (N + 1)
    for i in range(N):
        B_count[B[i]] += 1

    #Cの各要素の出現回数を数える
    C_count = [0] * (N + 1)
    for i in range(N):
        C_count[C[i]] += 1

    #Bの各要素の出現回数を数える
    B_count = [0] * (N + 1)
    for i in range(N):
        B_count[B[i]] += 1

    ans = 0
    for i in range(1, N + 1):
        ans += A_count[i] * C_count[i] * B_count[i]

    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # Bを要素番号とするリストを作成
    B_list = [0] * (N + 1)
    for i in range(N):
        B_list[B[i]] = i

    # Cの各要素をBの要素番号に変換
    C_list = [0] * N
    for i in range(N):
        C_list[i] = B_list[C[i]]

    # C_listをソート
    C_list.sort()

    # Aの各要素の値をBの要素番号に変換
    A_list = [0] * N
    for i in range(N):
        A_list[i] = B_list[A[i]]

    # A_listをソート
    A_list.sort()

    # A_listとC_listの各要素を比較して、条件を満たす組の数をカウント
    count = 0
    for i in range(N):
        # A_listの要素以上の値を持つ最初のC_listの要素のインデックスを取得
        index = binary_search(C_list, A_list[i])

        # A_listの要素がC_listに含まれている場合
        if index != -1:
            count += N - index

    print(count)
