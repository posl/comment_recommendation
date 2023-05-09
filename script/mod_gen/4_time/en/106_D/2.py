def main():
    n, m, q = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(m)]
    pq = [list(map(int, input().split())) for _ in range(q)]
    lr.sort(key=lambda x: x[1])
    for i in range(q):
        p, q = pq[i]
        cnt = 0
        for j in range(m):
            if lr[j][0] >= p and lr[j][1] <= q:
                cnt += 1
        print(cnt)
    return

if __name__ == '__main__':
    main()