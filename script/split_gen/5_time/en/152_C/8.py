def main():
    N = int(input())
    P = list(map(int, input().split()))
    P = [0] + P
    ans = 0
    min = N + 1
    for i in range(1, N + 1):
        if P[i] < min:
            ans += 1
            min = P[i]
    print(ans)
