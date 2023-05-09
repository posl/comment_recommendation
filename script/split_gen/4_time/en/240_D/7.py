def main():
    N = int(input())
    balls = list(map(int, input().split()))
    ans = [0] * N
    ans[0] = 1
    for i in range(1, N):
        ans[i] = ans[i-1]
        if balls[i-1] == ans[i]:
            ans[i] += 1
    for i in range(N):
        print(ans[i])
main()
