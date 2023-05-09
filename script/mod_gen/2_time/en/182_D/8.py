def main():
    N = int(input())
    A = list(map(int, input().split()))
    if sum(A) <= 0:
        print(0)
        return
    for i in range(1, N):
        A[i] += A[i-1]
    print(max(A))

if __name__ == '__main__':
    main()