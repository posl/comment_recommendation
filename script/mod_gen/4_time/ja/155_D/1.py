def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A_plus = []
    A_minus = []
    for i in range(N):
        if A[i] > 0:
            A_plus.append(A[i])
        else:
            A_minus.append(A[i])
    # print(A_plus, A_minus)
    A_plus.reverse()
    num = 0
    if K <= len(A_plus) * len(A_minus):
        for i in range(len(A_plus)):
            for j in range(len(A_minus)):
                num += 1
                if num == K:
                    print(A_plus[i] * A_minus[j])
                    exit()
    else:
        K -= len(A_plus) * len(A_minus)
        for i in range(len(A_plus)):
            for j in range(i + 1, len(A_plus)):
                num += 1
                if num == K:
                    print(A_plus[i] * A_plus[j])
                    exit()
        for i in range(len(A_minus)):
            for j in range(i + 1, len(A_minus)):
                num += 1
                if num == K:
                    print(A_minus[i] * A_minus[j])
                    exit()
        print(0)
        exit()

if __name__ == '__main__':
    main()