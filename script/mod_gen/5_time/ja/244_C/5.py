def main():
    N = int(input())
    A = 1
    B = 2*N + 1
    while True:
        print(A)
        A = int(input())
        if A == 0:
            break
        print(B)
        B = int(input())
        if B == 0:
            break

if __name__ == '__main__':
    main()