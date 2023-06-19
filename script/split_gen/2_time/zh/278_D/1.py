def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))
    # 初始值
    sum = 0
    for i in range(n):
        sum += a[i]
    # 处理
    for query in queries:
        if query[0] == 1:
            sum += query[1] * n
        elif query[0] == 2:
            sum += query[2]
        else:
            print(sum)
