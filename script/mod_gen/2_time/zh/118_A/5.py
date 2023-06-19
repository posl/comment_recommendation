def main():
    A,B = map(int,input().split())
    if A % B == 0:
        print(A+B)
    else:
        print(B-A)

if __name__ == '__main__':
    main()