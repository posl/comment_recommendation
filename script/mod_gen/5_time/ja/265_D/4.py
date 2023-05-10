def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    if N == 2:
        if A[0] + A[1] == P and A[0] + A[1] == Q and A[0] + A[1] == R:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

if __name__ == '__main__':
    main()