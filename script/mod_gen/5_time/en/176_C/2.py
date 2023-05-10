def main():
    N = int(input())
    A = list(map(int, input().split()))
    stools = [0] * N
    for i in range(N-1):
        if A[i+1] > A[i]:
            stools[i+1] = stools[i] + A[i+1] - A[i]
    print(sum(stools))

if __name__ == '__main__':
    main()