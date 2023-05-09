def solve():
    N = int(input())
    N_len = len(str(N))
    ans = 0
    for i in range(1,N+1):
        if i % 10 == 0:
            continue
        i_str = str(i)
        for j in range(1,N+1):
            if j % 10 == 0:
                continue
            j_str = str(j)
            if i_str[0] == j_str[-1] and i_str[-1] == j_str[0]:
                ans += 1
    print(ans)
    return 0
