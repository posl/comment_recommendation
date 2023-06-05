def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    count = 0
    for i in range(1, N):
        if H[i] > H[i-1]:
            count = 0
        else:
            count += 1
        ans = max(ans, count)
    print(ans)
