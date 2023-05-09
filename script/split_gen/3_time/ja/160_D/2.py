def main():
    N, X, Y = map(int, input().split())
    for k in range(1, N):
        ans = 0
        for i in range(1, N):
            for j in range(i + 1, N + 1):
                if i < X and X < j < Y and j - i == k:
                    ans += 1
                elif X < i < Y and Y < j and j - i == k:
                    ans += 1
                elif i < X and X < j < Y and j - i == k + 1:
                    ans += 1
                elif X < i < Y and Y < j and j - i == k + 1:
                    ans += 1
                elif i < X and X < j < Y and j - i > k + 1:
                    ans += 2
                elif X < i < Y and Y < j and j - i > k + 1:
                    ans += 2
                elif i < X and X < j < Y and j - i < k:
                    ans += 0
                elif X < i < Y and Y < j and j - i < k:
                    ans += 0
                elif i < X and X < j < Y and j - i == k:
                    ans += 1
                elif X < i < Y and Y < j and j - i == k:
                    ans += 1
                elif i < X and X < j < Y and j - i == k + 1:
                    ans += 1
                elif X < i < Y and Y < j and j - i == k + 1:
                    ans += 1
                elif i < X and X < j < Y and j - i > k + 1:
                    ans += 2
                elif X < i < Y and Y < j and j - i > k + 1:
                    ans += 2
                elif i < X and X < j < Y and j - i < k:
                    ans += 0
                elif X < i < Y and Y < j and j - i < k:
                    ans += 0
        print(ans)
