def main():
    A,B,K = map(int,input().split())
    if K <= A:
        A -= K
    else:
        B -= K - A
        A = 0
        if B < 0:
            B = 0
    print(A,B)

if __name__ == '__main__':
    main()