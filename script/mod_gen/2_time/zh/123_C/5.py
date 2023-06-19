def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    x = min(A, B, C, D, E)
    if N % x == 0:
        print(N // x + 4)
    else:
        print(N // x + 5)

if __name__ == '__main__':
    main()