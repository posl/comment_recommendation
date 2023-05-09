def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    max1 = max(A)
    max2 = sorted(A)[-2]
    for i in range(N):
        if A[i] == max1:
            print(max2)
        else:
            print(max1)

if __name__ == '__main__':
    main()