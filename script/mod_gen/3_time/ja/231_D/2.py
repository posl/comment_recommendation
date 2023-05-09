def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = [a - 1 for a in A]
    B = [b - 1 for b in B]
    if N == 2:
        if M == 0:
            print('Yes')
            return
        else:
            print('No')
            return
    if M == 0:
        print('Yes')
        return
    if M == 1:
        if A[0] == 0 or B[0] == 0:
            print('Yes')
            return
        if A[0] == N - 1 or B[0] == N - 1:
            print('Yes')
            return
        print('No')
        return
    if M == 2:
        if A[0] == 0 or B[0] == 0:
            if A[1] == 0 or B[1] == 0:
                print('Yes')
                return
            else:
                print('No')
                return
        if A[0] == N - 1 or B[0] == N - 1:
            if A[1] == N - 1 or B[1] == N - 1:
                print('Yes')
                return
            else:
                print('No')
                return
        print('No')
        return
    print('Yes')
main()

if __name__ == '__main__':
    main()