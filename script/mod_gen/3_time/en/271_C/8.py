def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - i
    for i in range(N):
        if B[i] < 0:
            print(i)
            return
    print(N)

if __name__ == '__main__':
    main()