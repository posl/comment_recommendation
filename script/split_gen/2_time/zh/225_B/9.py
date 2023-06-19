def main():
    n = int(input())
    edges = []
    for _ in range(n-1):
        a, b = map(int, input().split())
        edges.append((a, b))
    # 从1开始遍历
    for i in range(1, n+1):
        # 顶点i的度
        d = 0
        for a, b in edges:
            if a == i or b == i:
                d += 1
        if d == n-1:
            print('Yes')
            break
    else:
        print('No')
