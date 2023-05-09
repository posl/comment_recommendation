def main():
    N = int(input())
    ans = 0
    for i in range(1, N):
        for j in range(1, N):
            if N - i * j > 0:
                ans += 1
            else:
                break
    print(ans)
