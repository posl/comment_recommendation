def main():
    N, M = map(int, input().split())
    Y = [0] * M
    P = [0] * M
    for i in range(M):
        P[i], Y[i] = map(int, input().split())
    # 2次元配列を用意する。県の数だけ行がある。県ごとに市が何個あるかわからないので、列は最大値を入れる。
    arr = [[0] * M for _ in range(N)]
    # 2次元配列に市を入れる。県ごとに市が何個あるかわからないので、市の番号を入れるときに、空いているところに入れる。
    for i in range(M):
        arr[P[i] - 1][i] = Y[i]
    # 2次元配列を県ごとにソートする。
    for i in range(N):
        arr[i].sort()
    # 2次元配列を県ごとに出力する。県ごとに市が何個あるかわからないので、市の番号を出力するときに、空いているところは飛ばす。
    for i in range(M):
        for j in range(N):
            if arr[j][i] == Y[i]:
                print("{:0=6}".format(j + 1) + "{:0=6}".format(i + 1))

if __name__ == '__main__':
    main()