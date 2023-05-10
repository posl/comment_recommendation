def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        if A[i] < 0:
            A[i] *= -1
            A[i+1] *= -1
    print(sum(A))

if __name__ == '__main__':
    main()