def main():
    N, M, K = map(int, input().split())
    #友達関係
    friend = [[] for _ in range(N + 1)]
    #ブロック関係
    block = [[] for _ in range(N + 1)]
    #友達候補
    candidate = [0] * (N + 1)
    #友達関係の数
    friend_num = [0] * (N + 1)
    #友達関係の数の最大値
    max_friend_num = 0
    #友達関係の数の最大値の人の数
    max_friend_num_people = 0
    #友達関係の数の最大値の人のリスト
    max_friend_num_people_list = []
    #友達候補の数
    candidate_num = [0] * (N + 1)
    #友達候補の数の最大値
    max_candidate_num = 0
    #友達候補の数の最大値の人の数
    max_candidate_num_people = 0
    #友達候補の数の最大値の人のリスト
    max_candidate_num_people_list = []
    #友達関係とブロック関係を入力
    for i in range(M):
        A, B = map(int, input().split())
        friend[A].append(B)
        friend[B].append(A)
        friend_num[A] += 1
        friend_num[B] += 1
    for i in range(K):
        C, D = map(int, input().split())
        block[C].append(D)
        block[D].append(C)
    #友達関係の数の最大値と最大値の人の数とリストを求める
    for i in range(1, N + 1):
        if max_friend_num < friend_num[i]:
            max_friend_num = friend_num[i]
            max_friend_num_people = 1
            max_friend_num_people_list = [i]
        elif max_friend_num == friend_num[i]:
            max_friend

if __name__ == '__main__':
    main()