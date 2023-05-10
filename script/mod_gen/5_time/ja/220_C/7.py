def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    sumA = sum(A)
    if X < sumA:
        print(0)
        return
    ans = (X // sumA) * N
    X %= sumA
    for i, a in enumerate(A):
        if X < 0:
            break
        X -= a
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()