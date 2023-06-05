def main():
    N, M = map(int, input().split())
    K = []
    A = []
    for i in range(N):
        K.append(int(input().split()[0]))
        A.append(list(map(int, input().split())))
    # print(K)
    # print(A)
    count = 0
    for i in range(1, M+1):
        for j in range(N):
            if i in A[j]:
                if j == N-1:
                    count += 1
            else:
                break
    print(count)

if __name__ == '__main__':
    main()