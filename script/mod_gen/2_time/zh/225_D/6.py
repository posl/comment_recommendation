def main():
    N, Q = map(int, input().split())
    carriages = [i for i in range(N)]
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            # 1 x y：把车y的前面和车x的后面连接起来。
            # 可以保证：
            # x ≠ y
            # 就在这个查询之前，没有火车连接到x号车的后面；
            # 就在这个查询之前，没有火车连接到y车的前面；
            # 就在这次查询之前，车x和车y属于不同的连接部件。
            x = query[1] - 1
            y = query[2] - 1
            if carriages[x] != carriages[y]:
                for j in range(N):
                    if carriages[j] == carriages[y]:
                        carriages[j] = carriages[x]
        elif query[0] == 2:
            # 2 x y：将车y的车头与车x的车尾断开连接。
            # 可以保证：
            # x ≠ y；
            # 就在这个查询之前，车y的前面与车x的后面直接相连。
            x = query[1] - 1
            y = query[2] - 1
            if carriages[x] == carriages[y]:
                for j in range(N):
                    if carriages[j] == carriages[x]:
                        carriages[j] = j
        elif query[0] == 3:
            # 3 x:打印属于包含车x的连接部件的车的车号，从前到后。
            x = query[1] - 1
            result = []
            for j in range(N):
                if carriages[j] == carriages[x]:
                    result.append(str(j + 1))
            print(len(result), ' '.join(result))

if __name__ == '__main__':
    main()