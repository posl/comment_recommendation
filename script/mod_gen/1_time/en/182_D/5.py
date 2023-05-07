def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += max(0, A[i])
    print(ans)
    return

if __name__ == '__main__':
    main()