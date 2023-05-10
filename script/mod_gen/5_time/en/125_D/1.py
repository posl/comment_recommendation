def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N-1):
        if A[i] < 0:
            count += 1
            A[i] *= -1
        if A[i+1] < 0:
            count += 1
            A[i+1] *= -1
    if count % 2 == 0:
        print(sum(A))
    else:
        print(sum(A) - 2*min(A))

if __name__ == '__main__':
    main()