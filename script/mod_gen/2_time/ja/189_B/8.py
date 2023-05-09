def main():
    N, X = map(int, input().split())
    ans = -1
    for i in range(N):
        v, p = map(int, input().split())
        X -= v * p / 100
        if X < 0:
            ans = i + 1
            break
    print(ans)

if __name__ == '__main__':
    main()