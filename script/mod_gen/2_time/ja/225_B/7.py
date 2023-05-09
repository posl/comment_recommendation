def main():
    #入力
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    #ノードの数をカウントする
    node = [0 for _ in range(N+1)]
    for a,b in AB:
        node[a] += 1
        node[b] += 1
    #ノードの数がN-1個のときはスター
    if node.count(N-1) == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()