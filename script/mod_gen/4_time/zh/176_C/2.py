def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    #print(N)
    #print(A)
    A.reverse()
    #print(A)
    res = 0
    for i in range(N):
        if A[i] > res:
            res = A[i]
        elif A[i] == res:
            res = A[i] - 1
        elif A[i] < res:
            res = A[i]
    print(res)

if __name__ == '__main__':
    main()