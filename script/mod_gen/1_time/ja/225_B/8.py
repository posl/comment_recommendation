def main():
    N = int(input())
    #各頂点の次数を格納するリスト
    deg = [0 for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        #頂点番号は1から始まっているので、1を引いて0から始まるようにする
        a -= 1
        b -= 1
        #a,bの次数をそれぞれ1増やす
        deg[a] += 1
        deg[b] += 1
    #次数がN-1の頂点が1つだけあればスター
    if deg.count(N-1) == 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()