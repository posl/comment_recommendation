def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
    elif N <= A:
        print(1)
    elif A < N <= A + B:
        print(2)
    else:
        a = (N - A) // (A + B)
        b = (N - A) % (A + B)
        print(A + a * A + b)

if __name__ == '__main__':
    main()