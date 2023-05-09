def solve():
    N = int(input())
    A = list(map(int, input().split()))
    maxA = max(A)
    A = set(A)
    ans = 0
    for i in range(1, maxA + 1):
        flag = True
        for j in range(2, maxA // i + 1):
            if i * j in A:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
    return 0
