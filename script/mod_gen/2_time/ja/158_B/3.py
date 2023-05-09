def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif A + B >= N:
        print(A)
    else:
        print((N // (A + B)) * A + min(A, N % (A + B)))
main()

if __name__ == '__main__':
    main()