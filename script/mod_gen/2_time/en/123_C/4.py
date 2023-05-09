def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_ = min(A, B, C, D, E)
    print((N + min_ - 1) // min_ + 4)

if __name__ == '__main__':
    main()