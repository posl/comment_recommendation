def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    # compute
    A.sort()
    B.sort()
    C.sort()
    cnt = 0
    i = 0
    j = 0
    k = 0
    while i<N and j<N and k<N:
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            cnt += 1
            i += 1
            j += 1
    print(cnt)

if __name__ == '__main__':
    main()