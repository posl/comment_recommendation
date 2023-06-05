def main():
    A,B,C,X = map(int, input().split())
    if A >= X:
        print(1.0)
        return
    if X > B:
        print(0.0)
        return
    if C == 0:
        print(0.0)
        return
    if A+1 == B:
        if X == A+1:
            print(1.0)
        else:
            print(0.0)
        return
    if X == A+1:
        print(1.0)
        return
    if X == B:
        print(1.0)
        return
    if X < A+C+1:
        print(1.0)
        return
    print(C/(B-A-1))
    return

if __name__ == '__main__':
    main()