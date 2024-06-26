def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(1, N):
        if H[i] <= H[i-1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    print(max(ans, cnt))

if __name__ == '__main__':
    main()