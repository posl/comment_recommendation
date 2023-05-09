def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    diff = 100
    for i in range(N):
        if abs(T - H[i] * 0.006 - A) < diff:
            ans = i + 1
            diff = abs(T - H[i] * 0.006 - A)
    print(ans)

if __name__ == '__main__':
    main()