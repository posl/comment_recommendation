def main():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    # 木の場合は、最大の隣接数+1が色の数になる
    max_adj = 0
    for i in range(n):
        adj = 0
        for j in range(n-1):
            if edges[j][0] == i+1 or edges[j][1] == i+1:
                adj += 1
        if max_adj < adj:
            max_adj = adj
    print(max_adj+1)
    for i in range(n-1):
        print(i%(max_adj+1)+1)
main()
