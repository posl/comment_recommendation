def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = list(set(A))
    A.sort()
    if A[0] != 0:
        print(0)
    else:
        for i in range(1, len(A)):
            if A[i] - A[i-1] != 1:
                print(A[i-1] + 1)
                return
        print(A[-1] + 1)

if __name__ == '__main__':
    main()