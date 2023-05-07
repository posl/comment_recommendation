def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if abs(A - (T - H[i] * 0.006)) < abs(A - (T - H[ans] * 0.006)):
            ans = i
    print(ans + 1)

if __name__ == '__main__':
    main()