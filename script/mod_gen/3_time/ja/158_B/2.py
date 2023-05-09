def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif A + B <= N:
        print((N // (A + B)) * A + min(N % (A + B), A))
    else:
        print(min(N, A))

if __name__ == '__main__':
    main()