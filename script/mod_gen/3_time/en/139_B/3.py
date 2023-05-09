def main():
    A, B = input().split()
    A = int(A)
    B = int(B)
    if B % A == 0:
        print(int(B/A))
    else:
        print(int(B/A)+1)

if __name__ == '__main__':
    main()