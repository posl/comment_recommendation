def solve():
    n = int(input())
    a = list(map(int, input().split()))
    # print(n)
    # print(a)
    # print(len(a))
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if min(a[i], a[j]) == i+1 and max(a[i], a[j]) == j+1:
                cnt += 1
    print(cnt)
solve()
