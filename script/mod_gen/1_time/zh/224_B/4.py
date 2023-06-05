def main():
    # 读入数据
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    # 判断
    for i1 in range(H):
        for i2 in range(i1+1, H):
            for j1 in range(W):
                for j2 in range(j1+1, W):
                    if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
                        print('No')
                        return
    print('Yes')
    return

if __name__ == '__main__':
    main()