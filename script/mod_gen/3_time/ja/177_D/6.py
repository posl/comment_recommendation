def main():
    n,m = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(m)]
    ab = sorted(ab, key=lambda x: x[0])
    ab = sorted(ab, key=lambda x: x[1])
    #print(ab)
    # 隣り合う要素が同じ値であるかどうかを確認する
    # 隣り合う要素が同じ値である場合、グループ数を1つ減らす
    cnt = 0
    for i in range(1,m):
        if ab[i-1][1] == ab[i][1]:
            cnt += 1
    #print(cnt)
    # グループ数は、m-1からcntを引いた値
    print(m-1-cnt)

if __name__ == '__main__':
    main()