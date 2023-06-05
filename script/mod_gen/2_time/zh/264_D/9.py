def main():
    # 读入矩阵A
    h1, w1 = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h1)]
    # 读入矩阵B
    h2, w2 = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(h2)]
    # 从矩阵A中删除行和列，使其等于矩阵B
    for i in range(h1 - h2 + 1):
        for j in range(w1 - w2 + 1):
            # 从矩阵A中删除行和列，使其等于矩阵B
            for k in range(h2):
                if a[i + k][j:j + w2] != b[k]:
                    break
            else:
                print('Yes')
                exit()
    print('No')

if __name__ == '__main__':
    main()