def main():
    N = int(input())
    H = [int(i) for i in input().split()]
    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if H[i] >= H[j]:
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()