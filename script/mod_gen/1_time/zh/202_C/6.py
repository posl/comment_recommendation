def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    D = [0] * (N + 1)
    for i in range(N):
        D[B[C[i]]] += 1
    print(sum([D[A[i]] for i in range(N)]))

if __name__ == '__main__':
    main()