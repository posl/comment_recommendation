def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    if N == 2:
        if M == 0:
            print('Yes')
        else:
            print('No')
        return
    if M == 0:
        print('Yes')
        return
    if N == 3:
        if M == 1:
            print('Yes')
        else:
            print('No')
        return
    if M == 1:
        print('Yes')
        return
    if M == 2:
        if A[0] == A[1] or B[0] == B[1]:
            print('Yes')
        else:
            print('No')
        return
    print('Yes')
main()

if __name__ == '__main__':
    main()