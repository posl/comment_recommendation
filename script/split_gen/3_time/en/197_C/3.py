def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(30):
        cnt = 0
        for j in range(N):
            if A[j] >> i & 1:
                cnt += 1
        ans |= (1 << i) * (cnt % 2)
    print(ans)
