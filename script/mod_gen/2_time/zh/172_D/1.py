def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    sum = 0
    i = 0
    j = 0
    #print(A, B)
    while True:
        if i < N and j < M:
            if A[i] <= B[j]:
                if sum + A[i] > K:
                    break
                else:
                    sum += A[i]
                    i += 1
            else:
                if sum + B[j] > K:
                    break
                else:
                    sum += B[j]
                    j += 1
        elif i < N:
            if sum + A[i] > K:
                break
            else:
                sum += A[i]
                i += 1
        elif j < M:
            if sum + B[j] > K:
                break
            else:
                sum += B[j]
                j += 1
        else:
            break
    print(i+j)

if __name__ == '__main__':
    main()