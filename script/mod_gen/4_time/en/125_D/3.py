def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] < 0 and A[-1] < 0:
        if N % 2 == 0:
            print(-sum(A))
        else:
            print(-sum(A) + 2 * A[0])
    elif A[0] < 0 and A[-1] >= 0:
        print(-sum(A))
    else:
        print(sum(A))

if __name__ == '__main__':
    main()