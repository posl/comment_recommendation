def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    while True:
        B = []
        for a in A:
            if a % 2 == 0:
                B.append(a // 2)
            elif a % 3 == 0:
                B.append(a // 3)
            else:
                B.append(a)
        if A == B:
            break
        A = B
        ans += 1
    for a in A:
        if a != A[0]:
            print(-1)
            return
    print(ans)
solve()
