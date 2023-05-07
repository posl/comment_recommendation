def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    ans = 0
    X = A[X]
    while X != 1:
        ans += 1
        X = A[X]
    ans += 1
    print(ans)

if __name__ == '__main__':
    main()