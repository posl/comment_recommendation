def main():
    A,B = input().split()
    A = int(A)
    B = int(B)
    count = 1
    while(A*B > A):
        A = A*B
        count = count + 1
    print(count)
main()

if __name__ == '__main__':
    main()