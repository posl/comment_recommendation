def main():
    # 读取输入
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(input().split())
    #print(queries)
    # 处理输入
    a = []
    for query in queries:
        if query[0] == '1':
            a.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            b = [i for i in a if i <= x]
            b.sort(reverse=True)
            if len(b) >= k:
                print(b[k-1])
            else:
                print(-1)
        else:
            x = int(query[1])
            k = int(query[2])
            b = [i for i in a if i >= x]
            b.sort()
            if len(b) >= k:
                print(b[k-1])
            else:
                print(-1)
    return
