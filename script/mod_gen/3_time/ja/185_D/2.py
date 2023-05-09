def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A + [N+1]
    A.sort()
    B = [A[i+1] - A[i] - 1 for i in range(M+1)]
    B = [i for i in B if i != 0]
    k = min(B)
    print((sum(B) + k - 1) // k)

if __name__ == '__main__':
    main()