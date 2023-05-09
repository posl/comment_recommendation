def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    count = [0] * N
    for i in range(N):
        for j in range(i+1, N):
            count[min(j-i, abs(X-i)+1+abs(Y-j), abs(Y-i)+1+abs(X-j))] += 1
    for i in range(1, N):
        print(count[i])

if __name__ == '__main__':
    main()