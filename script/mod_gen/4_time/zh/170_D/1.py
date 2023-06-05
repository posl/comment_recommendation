def main():
    N = int(input())
    A = list(map(int, input().split()))
    # print(N)
    # print(A)
    # print(A[0])
    cnt = 0
    for i in range(N):
        # print(i)
        # print(A[i])
        # print(A[i+1:])
        if i == 0:
            if A[i] not in A[i+1:]:
                cnt += 1
        elif i == N-1:
            if A[i] not in A[:i]:
                cnt += 1
        else:
            if A[i] not in A[:i] and A[i] not in A[i+1:]:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()