def main():
    A,B,C,D = map(int, input().split())
    if B > A:
        A, B = B, A
    if C > D:
        C, D = D, C
    if A > D * B:
        print(-1)
        return
    if B == 0:
        print(0)
        return
    if C == 0:
        print(-1)
        return
    i = 0
    while A > D * B:
        A += C
        B += D
        i += 1
    print(i)

if __name__ == '__main__':
    main()