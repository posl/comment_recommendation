def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    diff = 10**10
    for i in range(N):
        if abs(A - (T - H[i] * 0.006)) < diff:
            diff = abs(A - (T - H[i] * 0.006))
            ans = i + 1
    print(ans)

if __name__ == '__main__':
    main()