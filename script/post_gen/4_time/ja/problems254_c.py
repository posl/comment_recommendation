Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N - K):
        if A[i] > A[i + K]:
            print("Yes")
            return
    print("No")

main()

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n-k):
        if a[i] > a[i+k]:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N-K):
        if A[i] > A[i+K]:
            print("No")
            return
    print("Yes")

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if n == k:
        if a == sorted(a):
            print("Yes")
        else:
            print("No")
        return
    for i in range(0, n - k):
        if a[i] > a[i + k]:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 5

def solve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 'Yes'
    for i in range(N-K):
        if A[i] > A[i+K]:
            ans = 'No'
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    B.sort()
    B.reverse()
    for i in range(K):
        if A[i] < B[i]:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if (a[-1] - a[0] <= k):
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = []
    for i in range(n-k):
        b.append(a[i+k-1]-a[i])
    if min(b) <= 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if N == K:
        print('Yes')
    else:
        A.sort()
        if A[-1] <= A[N-K-1]:
            print('No')
        else:
            print('Yes')
main()

=======
Suggestion 10

def main():
    # データ入力
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # ソート後の配列
    A_sort = sorted(A)

    # 交換回数
    change_count = 0

    # ソート後の配列の要素数分ループ
    for i in range(N):
        # ソート後の配列の要素と元の配列の要素が一致しない場合
        if A_sort[i] != A[i]:
            # 交換回数をカウントアップ
            change_count += 1

    # 交換回数がK以下の場合
    if change_count <= K:
        # Yesを出力
        print("Yes")
    else:
        # Noを出力
        print("No")
