def main():
    # 读取输入
    line = input()
    n, m, q = [int(i) for i in line.split()]
    trains = []
    for i in range(m):
        line = input()
        l, r = [int(j) for j in line.split()]
        trains.append([l, r])
    queries = []
    for i in range(q):
        line = input()
        p, q = [int(j) for j in line.split()]
        queries.append([p, q])
    # 计算
    trains.sort(key=lambda x: x[0])
    trains.sort(key=lambda x: x[1])
    queries.sort(key=lambda x: x[0])
    queries.sort(key=lambda x: x[1])
    for query in queries:
        count = 0
        for train in trains:
            if query[0] <= train[0] and train[1] <= query[1]:
                count += 1
        print(count)
