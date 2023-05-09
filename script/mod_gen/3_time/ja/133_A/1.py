def main():
    N, A, B = map(int, input().split())
    if A * N > B:
        print(B)
    else:
        print(A * N)

if __name__ == '__main__':
    main()