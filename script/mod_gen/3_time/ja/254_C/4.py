def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if N == 2:
        print('Yes' if A[0] == A[1] else 'No')
    elif N == 3:
        if A[0] == A[1] or A[1] == A[2]:
            print('Yes')
        else:
            print('No')
    else:
        if A[0] == A[1] or A[1] == A[2]:
            print('Yes')
        elif A[0] != A[1] and A[1] != A[2]:
            print('No')
        else:
            if A[1] == A[2]:
                if A[2] == A[3]:
                    print('Yes')
                elif A[2] != A[3]:
                    print('No')
            elif A[0] == A[1]:
                if A[1] == A[2]:
                    print('Yes')
                elif A[1] != A[2]:
                    print('No')

if __name__ == '__main__':
    main()