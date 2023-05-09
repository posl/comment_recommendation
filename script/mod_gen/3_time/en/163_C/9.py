def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    B = [0] * (N + 1)
    for i in range(N):
        B[A[i + 1]] += 1
    for i in range(1, N + 1):
        print(B[i])

if __name__ == '__main__':
    main()