def main():
    n, m, q = map(int, input().split())
    lr = []
    for i in range(m):
        lr.append(list(map(int, input().split())))
    pq = []
    for i in range(q):
        pq.append(list(map(int, input().split())))
    for i in range(q):
        count = 0
        for j in range(m):
            if pq[i][0] <= lr[j][0] and lr[j][1] <= pq[i][1]:
                count += 1
        print(count)

if __name__ == '__main__':
    main()