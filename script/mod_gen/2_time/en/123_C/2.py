def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_time = min(A, B, C, D, E)
    print((N + min_time - 1) // min_time + 4)

if __name__ == '__main__':
    main()