def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif B == 0:
        print(N)
    else:
        print(A * (N // (A + B)) + min(A, N % (A + B)))

if __name__ == '__main__':
    main()