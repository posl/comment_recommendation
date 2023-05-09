def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    print(' '.join(str(b) for b in B))

if __name__ == '__main__':
    main()