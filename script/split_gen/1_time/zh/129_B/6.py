def main():
    n = int(input())
    W = list(map(int, input().split()))
    min_diff = 100 * 100
    for i in range(1, n):
        diff = abs(sum(W[:i]) - sum(W[i:]))
        min_diff = min(min_diff, diff)
    print(min_diff)
