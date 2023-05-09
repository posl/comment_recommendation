def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N-1):
        A[i+1] = A[i+1] - A[i]
    print(A[-1])

if __name__ == '__main__':
    main()