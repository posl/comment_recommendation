def solve():
    N = int(input())
    v_list = list(map(int, input().split()))
    v_list.sort()
    ans = v_list[0]
    for i in range(1, N):
        ans = (ans + v_list[i]) / 2
    print(ans)
