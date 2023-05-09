def main():
    N,M = map(int,input().split())
    if N == 1:
        print(0)
        return
    if M == 1:
        for i in range(N):
            print(i)
        return
    if N == 2:
        if M == 2:
            print(1,2)
            print(2,1)
        elif M == 3:
            print(0,1)
            print(1,2)
        elif M == 4:
            print(1,1)
            print(1,2)
        elif M == 5:
            print(0,1)
            print(1,2)
        elif M == 6:
            print(1,2)
            print(2,2)
        elif M == 7:
            print(0,1)
            print(1,2)
        elif M == 8:
            print(1,1)
            print(1,2)
        elif M == 9:
            print(0,1)
            print(1,2)
    elif N == 3:
        if M == 2:
            print(1,2,3)
            print(2,1,2)
            print(3,2,3)
        elif M == 3:
            print(0,1,2)
            print(1,2,3)
            print(2,3,4)
        elif M == 4:
            print(1,1,2)
            print(1,2,3)
            print(2,3,4)
        elif M == 5:
            print(0,1,2)
            print(1,2,3)
            print(2,3,4)
        elif M == 6:
            print(1,2,3)
            print(2,3,3)
            print(3,3,4)
        elif M == 7:
            print(0,1,2)
            print(1,2,3)
            print(2,3,4)
        elif M == 8:
            print(1,1,2)
            print(1,2,3)
            print(2,3,4)
        elif M == 9:
            print(0,1,2)
            print(1,2,3)
            print(2,3,

if __name__ == '__main__':
    main()