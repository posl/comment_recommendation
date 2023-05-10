def main():
    N = int(input())
    ans = N
    for i in range(1, N+1):
        cnt = 0
        tmp = i
        while tmp < N:
            tmp *= i
            cnt += 1
        ans = min(ans, cnt + (N - tmp))
    print(ans)
