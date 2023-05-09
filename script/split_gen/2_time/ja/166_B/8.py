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
