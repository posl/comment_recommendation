def main():
    N, M, K = map(int, input().split())
    friend = [list(map(int, input().split())) for _ in range(M)]
    block = [list(map(int, input().split())) for _ in range(K)]
    #友達関係をリスト化
    friend_list = [[] for _ in range(N+1)]
    for f in friend:
        friend_list[f[0]].append(f[1])
        friend_list[f[1]].append(f[0])
    #ブロック関係をリスト化
    block_list = [[] for _ in range(N+1)]
    for b in block:
        block_list[b[0]].append(b[1])
        block_list[b[1]].append(b[0])
    #友達候補の数を計算
    for i in range(1, N+1):
        #友達候補の数 = 友達関係の数 - ブロック関係の数 - 自分自身
        ans = len(friend_list[i]) - len(block_list[i]) - 1
        print(ans, end=" ")

if __name__ == '__main__':
    main()