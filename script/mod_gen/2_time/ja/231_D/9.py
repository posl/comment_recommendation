def main():
    N, M = map(int, input().split())
    # 隣り合っている人を記録するリスト
    # 例えば、1と3が隣り合っているなら、[1,3]と[3,1]の両方を記録する
    neighbor = []
    # 1からNまでのリスト
    num = [i for i in range(1, N+1)]
    for i in range(M):
        A, B = map(int, input().split())
        neighbor.append([A, B])
        neighbor.append([B, A])
    # 隣り合っている人を順番に取り出す
    for i in range(len(neighbor)):
        # 隣り合っている人の位置を取得
        pos1 = num.index(neighbor[i][0])
        pos2 = num.index(neighbor[i][1])
        # 位置が隣り合っていない場合はNoを出力して終了
        if abs(pos1 - pos2) != 1:
            print('No')
            return
    # 隣り合っている人の位置が隣り合っている場合はYesを出力
    print('Yes')

if __name__ == '__main__':
    main()