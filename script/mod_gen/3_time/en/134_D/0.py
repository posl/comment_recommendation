def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(N, 0, -1):
        cnt = 0
        for j in range(i, N+1, i):
            if j in ans:
                cnt += 1
        if cnt % 2 != a[i-1]:
            ans.append(i)
    print(len(ans))
    print(*ans)

if __name__ == '__main__':
    main()