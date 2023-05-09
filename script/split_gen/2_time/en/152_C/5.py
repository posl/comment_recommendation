def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    min_val = 10**9
    for i in range(N):
        if P[i] <= min_val:
            ans += 1
            min_val = P[i]
    print(ans)
