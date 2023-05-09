def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min = min(A, B, C, D, E)
    print((N + min - 1) // min + 4)

if __name__ == '__main__':
    main()