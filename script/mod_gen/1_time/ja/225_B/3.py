def main():
    # 入力
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    
    # 処理
    # 頂点の次数を求める
    deg = [0] * (N+1)
    for i in range(N-1):
        deg[a[i]] += 1
        deg[b[i]] += 1
    
    # 出力
    if deg.count(N-1) == 1 and deg.count(1) == N-1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()