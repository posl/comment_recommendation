def main():
    A, B, K = map(int, input().split())
    if A > K:
        A -= K
        print(A, B)
    else:
        K -= A
        A = 0
        if B > K:
            B -= K
            print(A, B)
        else:
            B = 0
            print(A, B)

if __name__ == '__main__':
    main()