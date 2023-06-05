def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    if N == 1:
        if A[0] == 1:
            print(1)
            print(1)
        else:
            print(0)
    elif N == 2:
        if A[0] == 0 and A[1] == 1:
            print(1)
            print(2)
        elif A[0] == 1 and A[1] == 0:
            print(1)
            print(1)
        elif A[0] == 1 and A[1] == 1:
            print(2)
            print(1, 2)
        else:
            print(0)
    else:
        #print('N = ', N)
        #print('A = ', A)
        #print('A[0] = ', A[0])
        #print('A[1] = ', A[1])
        #print('A[2] = ', A[2])
        #print('A[3] = ', A[3])
        if A[0] == 1:
            if A[1] == 0 and A[2] == 0 and A[3] == 0:
                print(1)
                print(1)
            elif A[1] == 1 and A[2] == 0 and A[3] == 0:
                print(2)
                print(1, 2)
            elif A[1] == 0 and A[2] == 1 and A[3] == 0:
                print(2)
                print(1, 3)
            elif A[1] == 0 and A[2] == 0 and A[3] == 1:
                print(2)
                print(1, 4)
            elif A[1] == 1 and A[2] == 1 and A[3] == 0:
                print(3)
                print(1, 2, 3)
            elif A[1] == 1 and A[2] == 0 and A[3] == 1:
                print(3)
                print(1, 2, 4)
            elif A[1] == 0 and A[2

if __name__ == '__main__':
    main()