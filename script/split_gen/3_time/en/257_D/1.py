def main():
    N = int(input())
    trampolines = []
    for _ in range(N):
        x, y, p = map(int, input().split())
        trampolines.append((x, y, p))
    print(solve(N, trampolines))
