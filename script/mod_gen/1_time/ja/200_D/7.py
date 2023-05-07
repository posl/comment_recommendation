def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 200で割った余りでグループ分け
    g = [[] for _ in range(200)]
    for i, x in enumerate(a):
        g[x % 200].append(i + 1)
    # 余りが等しい組み合わせがあれば出力
    for x in g:
        if len(x) >= 2:
            print('Yes')
            print(1, x[0])
            print(1, x[1])
            return
    # 余りが等しい組み合わせがなければ、
    # 余りが等しい数列を2つ作る
    for i in range(200):
        for j in range(i + 1, 200):
            if len(g[i]) >= 1 and len(g[j]) >= 1:
                print('Yes')
                print(len(g[i]), *g[i])
                print(len(g[j]), *g[j])
                return
    print('No')

if __name__ == '__main__':
    main()