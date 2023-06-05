def main():
    n,m,q = map(int,input().split())
    lr = [tuple(map(int,input().split())) for _ in range(m)]
    pq = [tuple(map(int,input().split())) for _ in range(q)]
    ans = [0 for _ in range(q)]
    for i in range(q):
        for j in range(m):
            if pq[i][0] <= lr[j][0] and lr[j][1] <= pq[i][1]:
                ans[i] += 1
    for i in range(q):
        print(ans[i])
main()
