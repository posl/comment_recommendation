def main():
    N = int(input())
    A = []
    B = []
    for n in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(N, A, B)
    D = [0] * (10**5 + 1)
    for n in range(N):
        D[A[n]] += 1
        D[A[n] + B[n]] -= 1
    #print(D)
    for i in range(1, 10**5 + 1):
        D[i] += D[i - 1]
    #print(D)
    E = [0] * (N + 1)
    for i in range(1, 10**5 + 1):
        E[D[i]] += 1
    #print(E)
    for i in range(1, N + 1):
        print(E[i], end=' ')
    print()

if __name__ == '__main__':
    main()