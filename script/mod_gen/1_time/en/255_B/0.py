def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    left = 0
    right = 10 ** 10
    for _ in range(100):
        mid = (left + right) / 2
        ok = False
        for i in range(N):
            if i + 1 in A:
                continue
            for j in range(i + 1, N):
                if j + 1 in A:
                    continue
                if (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2 <= mid ** 2:
                    ok = True
        if ok:
            right = mid
        else:
            left = mid
    print(left)

if __name__ == '__main__':
    main()