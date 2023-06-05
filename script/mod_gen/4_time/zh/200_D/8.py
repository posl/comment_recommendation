def main():
    N = int(input())
    A = input().split()
    A = [int(i) for i in A]
    if N == 2:
        if A[0] % 200 == A[1] % 200:
            print('Yes')
            print(1, 1)
            print(1, 2)
        else:
            print('No')
    else:
        print('Yes')
        print(1, 1)
        print(2, 2, 3)

if __name__ == '__main__':
    main()