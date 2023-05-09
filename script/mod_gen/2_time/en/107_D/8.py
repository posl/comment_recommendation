def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print(N)
    #print(A)
    if N % 2 == 0:
        print(A[N // 2 - 1])
    else:
        print(A[N // 2])

if __name__ == '__main__':
    main()