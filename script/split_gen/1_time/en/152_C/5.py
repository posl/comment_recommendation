def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    min = N + 1
    for i in range(N):
        if P[i] <= min:
            ans += 1
            min = P[i]
    print(ans)
