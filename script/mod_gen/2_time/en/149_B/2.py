def main():
    A, B, K = map(int, input().split())
    if A > K:
        A -= K
    else:
        K -= A
        A = 0
        if B > K:
            B -= K
        else:
            B = 0
    print(A, B)
main()

if __name__ == '__main__':
    main()