def main():
    N, X, Y = list(map(int, input().split()))
    distance = [0] * N
    for i in range(1, N):
        for j in range(i+1, N+1):
            d = min(j-i, abs(X-i)+1+abs(Y-j))
            distance[d] += 1
    for i in range(1, N):
        print(distance[i])

if __name__ == '__main__':
    main()