def func():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 1
    for i in range(1, n):
        count = 1
        j = i
        while p[j-1] != 0:
            j = p[j-1]
            count += 1
        if count > ans:
            ans = count
    print(ans)
