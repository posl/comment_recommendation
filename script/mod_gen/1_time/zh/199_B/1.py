def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    min = max(A)
    max = min
    for i in range(N):
        if A[i] > min:
            min = A[i]
        if B[i] < max:
            max = B[i]
    if max < min:
        print(0)
    else:
        print(max - min + 1)

if __name__ == '__main__':
    main()