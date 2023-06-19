def main():
    # 读取输入
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(input().split())
    # 处理
    s = []
    for query in queries:
        if query[0] == '1':
            s.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            c = int(query[2])
            for i in range(c):
                if x in s:
                    s.remove(x)
                else:
                    break
        elif query[0] == '3':
            print(max(s) - min(s))
