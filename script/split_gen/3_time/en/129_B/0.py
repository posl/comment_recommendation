def main():
    N = int(input())
    W = list(map(int, input().split()))
    ans = float('inf')
    for i in range(N):
        ans = min(ans, abs(sum(W[:i+1]) - sum(W[i+1:])))
    print(ans)
