def main():
    N = int(input())
    S = [input() for i in range(N)]
    # 連続する黒のマスの数を数える
    def count_black(i, j, di, dj):
        count = 0
        while 0 <= i < N and 0 <= j < N:
            if S[i][j] == '#':
                count += 1
            else:
                break
            i += di
            j += dj
        return count
    # すべてのマスについて、8方向について黒のマスが6個以上連続しているかどうかをチェック
    for i in range(N):
        for j in range(N):
            if S[i][j] == '.':
                continue
            for di, dj in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                if count_black(i, j, di, dj) + count_black(i, j, -di, -dj) >= 7:
                    print('Yes')
                    return
    print('No')
