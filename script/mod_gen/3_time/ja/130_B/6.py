def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(1, N+1):
        D.append(D[i-1] + L[i-1])
    cnt = 0
    for i in range(N+1):
        if D[i] <= X:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()