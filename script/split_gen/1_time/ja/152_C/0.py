def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 1
    min = P[0]
    for i in range(1, N):
        if P[i] <= min:
            ans += 1
            min = P[i]
    print(ans)
