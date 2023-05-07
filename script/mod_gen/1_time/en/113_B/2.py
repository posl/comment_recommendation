def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    diff = 1000
    for i in range(N):
        tmp = T - H[i]*0.006
        if abs(tmp - A) < diff:
            diff = abs(tmp - A)
            ans = i + 1
    print(ans)

if __name__ == '__main__':
    main()