def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    if N == 1:
        if A[0] == 1:
            print(1)
        else:
            print(0)
        return
    A.sort()
    if A[0] != 1:
        print(0)
        return
    for i in range(N-1):
        if A[i+1] - A[i] > 1:
            print(A[i])
            return
    print(A[-1])

if __name__ == '__main__':
    main()