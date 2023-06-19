def solve(N, D, L, R):
    # print(N, D, L, R)
    # print("L", L)
    # print("R", R)
    # print("L", L)
    # print("R", R)
    # print("L", L)
    # print("R", R)
    L.sort()
    R.sort()
    # print("L", L)
    # print("R", R)
    ans = 0
    i = 0
    j = 0
    while i < N and j < N:
        if L[i] <= R[j]:
            ans += 1
            i += 1
        else:
            ans -= 1
            j += 1
    return ans
