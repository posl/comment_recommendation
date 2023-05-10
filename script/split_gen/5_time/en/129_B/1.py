def main():
    N = int(input())
    W = list(map(int, input().split()))
    result = 10000
    for i in range(1, N):
        result = min(result, abs(sum(W[:i]) - sum(W[i:])))
    print(result)
