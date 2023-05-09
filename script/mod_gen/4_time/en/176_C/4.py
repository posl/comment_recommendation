def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    stools = [0] * N
    stools[0] = A[0]
    for i in range(1, N):
        if A[i] <= stools[i-1]:
            stools[i] = A[i]
        else:
            stools[i] = stools[i-1]
    print(sum(stools))

if __name__ == '__main__':
    main()