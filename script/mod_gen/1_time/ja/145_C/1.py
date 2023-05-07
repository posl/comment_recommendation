def main():
    N = int(input())
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    
    # 順列を列挙する
    import itertools
    order = list(itertools.permutations(range(N)))
    
    # 経路の長さの総和
    total = 0
    for o in order:
        for i in range(N-1):
            x1, y1 = X[o[i]], Y[o[i]]
            x2, y2 = X[o[i+1]], Y[o[i+1]]
            total += ((x1-x2)**2+(y1-y2)**2)**0.5
    
    # 平均
    ave = total / len(order)
    print(ave)

if __name__ == '__main__':
    main()