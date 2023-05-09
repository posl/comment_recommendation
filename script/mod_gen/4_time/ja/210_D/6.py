def main():
    # 標準入力の取得
    h,w,c = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    # 処理
    min_cost = 10 ** 9 + 1
    for i1 in range(h):
        for j1 in range(w):
            for i2 in range(h):
                for j2 in range(w):
                    if i1 == i2 and j1 == j2:
                        continue
                    cost = a[i1][j1] + a[i2][j2] + c * (abs(i1-i2) + abs(j1-j2))
                    if cost < min_cost:
                        min_cost = cost
    # 標準出力
    print(min_cost)

if __name__ == '__main__':
    main()