def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    S = input()
    # LとRで分ける
    L = []
    R = []
    for i in range(N):
        if S[i] == 'L':
            L.append(XY[i])
        else:
            R.append(XY[i])
    # X座標でソート
    L.sort()
    R.sort()
    # 衝突判定
    for i in range(len(L)):
        for j in range(len(R)):
            if L[i][1] == R[j][1] and L[i][0] < R[j][0]:
                print('Yes')
                exit()
    print('No')

if __name__ == '__main__':
    main()