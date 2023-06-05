def main():
    N,Q = map(int,input().split())
    query = []
    for i in range(Q):
        query.append(list(map(int,input().split())))
    #print(N,Q)
    #print(query)
    # 连接部件
    parts = []
    for i in range(N):
        parts.append([i+1])
    #print(parts)
    # 处理查询
    for i in range(Q):
        if query[i][0] == 1:
            # 1 x y：把车y的前面和车x的后面连接起来。
            # 可以保证：
            # x ≠ y
            # 就在这个查询之前，没有火车连接到x号车的后面；
            # 就在这个查询之前，没有火车连接到y车的前面；
            # 就在这次查询之前，车x和车y属于不同的连接部件。
            x = query[i][1]
            y = query[i][2]
            #print("1",x,y)
            #print(parts)
            #print(parts[x-1])
            #print(parts[y-1])
            #print(parts[x-1] == parts[y-1])
            if parts[x-1] != parts[y-1]:
                parts[x-1] = parts[x-1] + parts[y-1]
                parts[y-1] = parts[x-1]
            #print(parts)
        if query[i][0] == 2:
            # 2 x y：将车y的车头与车x的车尾断开连接。
            # 可以保证：
            # x ≠ y；
            # 就在这个查询之前，车y的前面与车x的后面直接相连。
            x = query[i][1]
            y = query[i][2]
            #print("2",x,y)
            #print(parts)
            #print(parts[x-1])
            #print(parts[y-1])
            #print(parts[x-1] == parts[y-1])
            if parts[x-1] == parts[y-1]:
                parts[x-1] = [x]
                parts[y-1] = [y]
            #print(parts)
        if query[i][0]
