def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min = 1e9
    for i in range(N):
        temp = T - H[i] * 0.006
        if min > abs(A - temp):
            min = abs(A - temp)
            ans = i + 1
    print(ans)

if __name__ == '__main__':
    main()