Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    d = [0] * K
    A = [0] * K
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))
    ans = N
    for i in range(K):
        ans -= len(A[i])
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    d = [0] * K
    A = [0] * K
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))

    ans = 0
    for i in range(K):
        for j in range(d[i]):
            if A[i][j] == 1:
                ans += 1
                break
    print(ans)

main()

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = [0] * N
    for i in range(K):
        d = int(input())
        for j in map(int, input().split()):
            A[j - 1] += 1
    print(A.count(0))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    d = []
    for i in range(K):
        d.append(int(input()))
    A = []
    for i in range(K):
        A.append(list(map(int, input().split())))

    ans = 0
    for i in range(1, N+1):
        for j in range(K):
            if i in A[j]:
                ans += 1
                break
    print(N-ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    cnt = [0 for i in range(N)]
    for i in range(K):
        d = int(input())
        for j in map(int, input().split()):
            cnt[j-1] += 1
    print(cnt.count(0))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    ans = 0
    for _ in range(K):
        d = int(input())
        A = list(map(int, input().split()))
        ans += N - d
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    d = [int(input()) for _ in range(K)]
    A = [[int(x) for x in input().split()] for _ in range(K)]
    #print(N, K, d, A)
    ans = 0
    for i in range(K):
        for j in range(d[i]):
            #print(A[i][j])
            if A[i][j] == 1:
                ans += 1
                break
    print(N - ans)
    return

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    #print(N, K)
    count = 0
    for i in range(K):
        d = int(input())
        #print(d)
        for j in range(d):
            A = int(input())
            #print(A)
            if A == 1:
                count += 1
                break
    print(N - count)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    # お菓子の種類数
    K = int(K)
    # お菓子を持っている人の数
    d = [0] * K
    # お菓子を持っている人のリスト
    A = [0] * K
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))
    # print(d)
    # print(A)
    # お菓子を持っている人のリストを集合に変換
    A_set = [set(A[i]) for i in range(K)]
    # print(A_set)
    # すぬけ君ごとに、お菓子を持っている人の集合を作成
    A_all = set()
    for i in range(K):
        A_all = A_all | A_set[i]
    # print(A_all)
    # すぬけ君ごとに、お菓子を持っている人の集合に含まれていない人の数をカウント
    count = 0
    for i in range(1, N + 1):
        if i not in A_all:
            count += 1
    print(count)

main()
