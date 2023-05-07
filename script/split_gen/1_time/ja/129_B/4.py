def main():
    N = int(input())
    W = [int(i) for i in input().split()]
    S = sum(W)
    ans = S
    for i in range(1, N):
        ans = min(ans, abs(2 * sum(W[:i]) - S))
    print(ans)
