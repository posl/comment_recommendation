def main():
    # 读取数据
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    # 读取查询
    query = []
    for i in range(q):
        x, k = map(int, input().split())
        query.append((x, k))
    # 处理查询
    for x, k in query:
        count = 0
        for i, num in enumerate(a):
            if num == x:
                count += 1
                if count == k:
                    print(i + 1)
                    break
        else:
            print(-1)
