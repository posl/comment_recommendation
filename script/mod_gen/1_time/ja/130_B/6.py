def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    d = 0
    ans = 0
    for i in range(N):
        d += L[i]
        if d <= X:
            ans += 1
        else:
            break
    print(ans + 1)

if __name__ == '__main__':
    main()