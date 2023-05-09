def main():
    A, B, C = input().split()
    A = int(A)
    B = int(B)
    C = int(C)
    if A * C > B:
        print(B // A)
    else:
        print(C)

if __name__ == '__main__':
    main()