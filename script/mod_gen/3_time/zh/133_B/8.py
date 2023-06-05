def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = sum((x-y)**2 for x, y in zip(X[i], X[j]))
            if int(dist**0.5)**2 == dist:
                count += 1
    print(count)

if __name__ == '__main__':
    main()