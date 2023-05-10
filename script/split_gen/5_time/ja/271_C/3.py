def solve():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0
    cnt = 0
    for i in range(N):
        if cnt >= N-1:
            break
        if a[i] == a[i+1]:
            cnt += 1
        else:
            cnt = 0
        ans += 1
    print(ans)
