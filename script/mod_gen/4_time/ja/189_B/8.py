def main():
    N, X = map(int, input().split())
    ans = -1
    for i in range(1, N+1):
        v, p = map(int, input().split())
        X -= v * p / 100
        if X < 0:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    main()