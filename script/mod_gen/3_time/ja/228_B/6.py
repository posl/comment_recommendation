def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    X = A[X]
    ans = 0
    while X != 1:
        X = A[X]
        ans += 1
    print(ans+1)

if __name__ == '__main__':
    main()