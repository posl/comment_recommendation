def main():
    X,A,D,N = map(int,input().split())
    if D == 0:
        if X == A:
            print(0)
        else:
            print("inf")
        return
    if N == 1:
        if X == A:
            print(0)
        else:
            print("inf")
        return
    if D > 0:
        if X < A or (X-A) % D != 0:
            print("inf")
            return
    else:
        if X > A or (X-A) % D != 0:
            print("inf")
            return
    if D > 0:
        if (X-A) // D >= 0:
            print((X-A) // D)
        else:
            print("inf")
    else:
        if (X-A) // D <= 0:
            print((X-A) // D)
        else:
            print("inf")

if __name__ == '__main__':
    main()