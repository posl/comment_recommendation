def main():
    N,A,B = map(int,input().split())
    if A == 0:
        print(0)
        return
    if B == 0:
        print(N)
        return
    if A + B > N:
        print(0)
        return
    if A + B == N:
        print(A)
        return
    if A + B < N:
        if A > B:
            print(B)
            return
        else:
            print(A)
            return

if __name__ == '__main__':
    main()