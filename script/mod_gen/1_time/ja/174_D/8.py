def main():
    N = int(input())
    c = input()
    # 石の色の配列を作成
    c_list = []
    for i in range(N):
        c_list.append(c[i])
    #print(c_list)
    # 赤い石の左隣に置かれた白い石の数をカウント
    count = 0
    for i in range(N-1):
        if c_list[i] == 'R' and c_list[i+1] == 'W':
            count += 1
    print(count)

if __name__ == '__main__':
    main()