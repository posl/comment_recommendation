def main():
    N, M, K = map(int, input().split())
    friends = []
    blocks = []
    for i in range(M):
        friends.append(list(map(int, input().split())))
    for i in range(K):
        blocks.append(list(map(int, input().split())))
    # print(friends)
    # print(blocks)
    # 人と人の友達候補の数を格納するリスト
    ans = [0] * N
    # 人と人の友達候補の数を格納するリスト
    # ans = [0 for i in range(N)]
    # print(ans)
    # 人と人の友達関係を格納するリスト
    friends_list = [[] for i in range(N)]
    # 人と人のブロック関係を格納するリスト
    blocks_list = [[] for i in range(N)]
    # print(friends_list)
    # print(blocks_list)
    # 友達関係
    for i in range(M):
        # 友達関係の人を格納
        friends_list[friends[i][0] - 1].append(friends[i][1] - 1)
        friends_list[friends[i][1] - 1].append(friends[i][0] - 1)
    # print(friends_list)
    # ブロック関係
    for i in range(K):
        # ブロック関係の人を格納
        blocks_list[blocks[i][0] - 1].append(blocks[i][1] - 1)
        blocks_list[blocks[i][1] - 1].append(blocks[i][0] - 1)
    # print(blocks_list)
    # 人と人の友達候補の数を格納
    for i in range(N):
        # 人と人の友達候補の数を格納
        ans[i] = N - len(friends_list[i]) - len(blocks_list[i]) - 1
        # 人と人の友達関係を格納
        for j in friends_list[i]:
            # 人と人の
