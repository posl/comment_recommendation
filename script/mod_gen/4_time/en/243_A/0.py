def main():
    V, A, B, C = map(int, input().split())
    if A > B:
        A, B = B, A
    if A > C:
        A, C = C, A
    if B > C:
        B, C = C, B
    if V < A:
        print('F')
    elif V < B:
        print('M')
    elif V < C:
        print('T')
    else:
        print('T')

if __name__ == '__main__':
    main()