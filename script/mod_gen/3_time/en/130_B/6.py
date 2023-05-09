def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    ans = 0
    d = 0
    for i in range(N+1):
        if d <= X:
            ans += 1
        d += L[i]
    print(ans)
main()

if __name__ == '__main__':
    main()