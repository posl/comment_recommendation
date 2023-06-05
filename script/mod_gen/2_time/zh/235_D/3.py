def solve():
    n, q = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    for i in range(q):
        x, k = [int(x) for x in input().split()]
        cnt = 0
        for j in range(n):
            if a[j] == x:
                cnt += 1
            if cnt == k:
                print(j+1)
                break
        else:
            print(-1)
solve()
