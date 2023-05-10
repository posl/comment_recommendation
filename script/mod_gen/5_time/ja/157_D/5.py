def main():
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    # 人iと人jの友達関係をグラフで表す
    friend = [[] for _ in range(N)]
    for A, B in AB:
        friend[A-1].append(B-1)
        friend[B-1].append(A-1)
    # 人iと人jのブロック関係をグラフで表す
    block = [[] for _ in range(N)]
    for C, D in CD:
        block[C-1].append(D-1)
        block[D-1].append(C-1)
    # 人iの友達候補の数を求める
    ans = [0] * N
    for i in range(N):
        ans[i] = len(set(friend[i]) - set(friend[i]) & set(block[i]) - {i} - set(friend[i]))
    print(*ans)

if __name__ == '__main__':
    main()