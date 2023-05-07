def solve(N):
    ans = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:int(len(str(i))/2)] == str(i)[int(len(str(i))/2):]:
                ans += 1
    return ans
