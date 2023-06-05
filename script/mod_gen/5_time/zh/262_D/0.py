def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if sum(a[i:j]) % (j - i) == 0:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()