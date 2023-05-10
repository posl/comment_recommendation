def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i+1 != a[i]:
            ans += 1
    if ans == N:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()