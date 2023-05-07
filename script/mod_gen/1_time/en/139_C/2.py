def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    cnt = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    print(ans)

if __name__ == '__main__':
    main()