def main():
    n,m = map(int,input().split())
    h = list(map(int,input().split()))
    ab = []
    for i in range(m):
        ab.append(list(map(int,input().split())))
    #print(n,m,h,ab)
    # 隣接リストを作成する
    # 1から始まるので、0番目はダミー
    adjacent_list = [[] for i in range(n+1)]
    for i in range(m):
        adjacent_list[ab[i][0]].append(ab[i][1])
        adjacent_list[ab[i][1]].append(ab[i][0])
    #print(adjacent_list)
    # 隣接リストを作成する
    # 1から始まるので、0番目はダミー
    adjacent_list = [[] for i in range(n+1)]
    for i in range(m):
        adjacent_list[ab[i][0]].append(ab[i][1])
        adjacent_list[ab[i][1]].append(ab[i][0])
    #print(adjacent_list)
    # 隣接する頂点の高さを比較する
    # 高ければ、goodでない
    # 低ければ、good
    # 1から始まるので、0番目はダミー
    good = 0
    for i in range(1,n+1):
        #print(i,adjacent_list[i])
        flag = True
        for j in adjacent_list[i]:
            if h[i-1] <= h[j-1]:
                flag = False
        if flag:
            good += 1
    print(good)

if __name__ == '__main__':
    main()