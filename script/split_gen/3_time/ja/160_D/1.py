def main():
    N, X, Y = map(int, input().split())
    for k in range(1, N):
        ans = 0
        for i in range(1, N+1):
            for j in range(i+1, N+1):
                if (i == X and j == Y) or (i == Y and j == X):
                    continue
                if abs(i-j) <= k:
                    ans += 1
                if abs(i-X) + abs(j-Y) <= k:
                    ans += 1
                if abs(i-Y) + abs(j-X) <= k:
                    ans += 1
        print(ans//2)
