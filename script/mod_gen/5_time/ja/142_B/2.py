def main():
    # 1行目の入力を受け取る
    # 入力値は文字列なので、split()でスペース区切りにし、map()でint型に変換してlist化する
    n, k = map(int, input().split())
    # 2行目の入力を受け取る
    h = list(map(int, input().split()))
    #print(n, k, h)
    count = 0
    for i in range(n):
        if h[i] >= k:
            count += 1
    print(count)
    return

if __name__ == '__main__':
    main()