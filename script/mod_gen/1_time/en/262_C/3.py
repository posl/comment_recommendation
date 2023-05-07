def main():
    N = int(input())
    A = list(map(int, input().split()))
    minA = [0] * N
    maxA = [0] * N
    for i in range(N):
        minA[i] = i + 1
        maxA[i] = i + 1
    for i in range(N):
        if minA[A[i] - 1] > i + 1:
            minA[A[i] - 1] = i + 1
        if maxA[A[i] - 1] < i + 1:
            maxA[A[i] - 1] = i + 1
    ans = 0
    for i in range(N):
        if minA[i] == i + 1 and maxA[i] == i + 1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()