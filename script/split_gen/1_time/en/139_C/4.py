def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    count = 0
    for i in range(1, N):
        if H[i-1] >= H[i]:
            count += 1
        else:
            count = 0
        ans = max(ans, count)
    print(ans)
