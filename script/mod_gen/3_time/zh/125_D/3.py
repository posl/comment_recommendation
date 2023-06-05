def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(N):
        if A[i] < 0:
            sum += -A[i]
        else:
            sum += A[i]
    if A[0] < 0:
        if N % 2 == 0:
            sum -= 2 * A[0]
        else:
            sum += 2 * A[0]
    print(sum)

if __name__ == '__main__':
    main()