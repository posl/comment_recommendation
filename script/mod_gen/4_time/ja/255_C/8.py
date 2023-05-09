def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        print(0)
        return
    if X == A:
        print(0)
        return
    if X < A:
        if D > 0:
            print(-1)
            return
        else:
            if (A - X) % D == 0:
                print((A - X) // D)
            else:
                print(-1)
            return
    if X > A:
        if D < 0:
            print(-1)
            return
        else:
            if (X - A) % D == 0:
                print((X - A) // D)
            else:
                print(-1)
            return

if __name__ == '__main__':
    main()