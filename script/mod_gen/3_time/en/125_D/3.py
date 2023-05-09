def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = A[i]
        if i % 2 == 0:
            B[i] = -B[i]
    print(max(sum(B), sum([-b for b in B])))

if __name__ == '__main__':
    main()