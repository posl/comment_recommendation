def main():
    N = int(input())
    S = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        a = 0
        b = 0
        for j in range(1, 1001):
            for k in range(1, j+1):
                if 4*j*k+3*j+3*k == S[i]:
                    a = j
                    b = k
        if a*b == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()