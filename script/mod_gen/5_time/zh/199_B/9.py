def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    min = 0
    max = 1000
    for i in range(N):
        if A[i] > min:
            min = A[i]
        if B[i] < max:
            max = B[i]
    if min > max:
        print(0)
    else:
        print(max - min + 1)

if __name__ == '__main__':
    main()