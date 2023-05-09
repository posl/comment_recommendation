def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A = [180, 186, 189, 191, 218]
    # N = 5
    # A = [123, 523]
    # N = 2
    # A = [2013, 1012, 2765, 2021, 508, 6971]
    # N = 6
    # 200で割った余り毎にグループ化
    groups = [[] for _ in range(200)]
    for i, a in enumerate(A):
        groups[a % 200].append(i)
    # 200で割った余りが同じグループが2つ以上あるなら、それらを出力
    for g in groups:
        if len(g) > 1:
            print('Yes')
            print(1, g[0] + 1)
            print(1, g[1] + 1)
            return
    # 200で割った余りが同じグループが2つもなければ、
    # 200で割った余りが同じグループがあるなら、それを使って2つのグループを作る
    for i, g in enumerate(groups):
        if len(g) > 0:
            for j, h in enumerate(groups):
                if len(h) > 0 and i != j:
                    print('Yes')
                    print(len(g), ' '.join(map(str, [x + 1 for x in g])))
                    print(len(h), ' '.join(map(str, [x + 1 for x in h])))
                    return
    # 200で割った余りが同じグループが1つもなければ、No
    print('No')

if __name__ == '__main__':
    main()