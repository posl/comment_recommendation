def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min = 100000
    for i in range(N):
        if abs(T - H[i] * 0.006 - A) < min:
            min = abs(T - H[i] * 0.006 - A)
            ans = i + 1
    print(ans)

if __name__ == '__main__':
    main()