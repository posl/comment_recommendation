def solve():
    N = int(input())
    A = list(map(int, input().split()))
    # 1からNまでの整数がそれぞれ何個あるか数える
    cnt = [0] * (N + 1)
    for a in A:
        cnt[a] += 1
    # 1からNまでの整数がそれぞれ何個あるか数えた結果、
    # 1からNまでの整数が1個ずつあるものを数える
    ans = 0
    for i in range(1, N + 1):
        if cnt[i] == 1:
            ans += 1
    # 1からNまでの整数が1個ずつあるものの個数を答える
    if ans == 0:
        print(-1)
    else:
        print(ans)
