def main():
    A, B, K = map(int, input().split())
    s = ''
    while A + B > 0:
        if A == 0:
            s += 'b'
            B -= 1
        elif B == 0:
            s += 'a'
            A -= 1
        else:
            # a が先頭にくる場合
            if K <= comb(A + B - 1, A - 1):
                s += 'a'
                A -= 1
            # b が先頭にくる場合
            else:
                s += 'b'
                K -= comb(A + B - 1, A - 1)
                B -= 1
    print(s)

if __name__ == '__main__':
    main()