def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif A + B == 0:
        print(N)
    else:
        print(N // (A + B) * A + min(A, N % (A + B)))

if __name__ == '__main__':
    main()