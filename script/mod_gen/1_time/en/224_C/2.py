def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                a = X[j] - X[i]
                b = Y[j] - Y[i]
                c = X[k] - X[i]
                d = Y[k] - Y[i]
                if a * d - b * c != 0:
                    ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()