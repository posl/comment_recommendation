def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    D = [0] * (N + 1)
    for i in range(N):
        D[A[i]] += 1
        D[A[i] + B[i]] -= 1
    for i in range(N):
        D[i + 1] += D[i]
    D = D[1:]
    D.sort()
    print(*D, sep=" ")

if __name__ == '__main__':
    main()