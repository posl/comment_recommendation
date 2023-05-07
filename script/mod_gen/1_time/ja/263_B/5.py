def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        ans = max(ans, P[i])
    print(ans)
    return

if __name__ == '__main__':
    main()