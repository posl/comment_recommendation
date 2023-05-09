def main():
    N = int(input())
    trampolines = [tuple(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans = max(ans, (abs(trampolines[i][0] - trampolines[j][0]) + abs(trampolines[i][1] - trampolines[j][1])) // (trampolines[i][2] + trampolines[j][2]) + 1)
    print(ans)
