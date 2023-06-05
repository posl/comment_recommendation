def main():
    #读入数据
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    #处理数据
    #行列都是白色的行列
    white_rows = [i for i in range(h) if all(a[i][j] == '.' for j in range(w))]
    white_cols = [j for j in range(w) if all(a[i][j] == '.' for i in range(h))]
    #输出数据
    for i in range(h):
        if i in white_rows:
            continue
        for j in range(w):
            if j in white_cols:
                continue
            print(a[i][j], end='')
        print()

if __name__ == '__main__':
    main()