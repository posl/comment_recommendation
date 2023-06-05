def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i == 0:
            ans += 1
        else:
            ans += (K-1)
    print(ans)

if __name__ == '__main__':
    main()