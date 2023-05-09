def main():
    A, B, K = map(int, input().split())
    ans = ""
    while A > 0 or B > 0:
        if B == 0:
            ans += "a"
            A -= 1
            continue
        if A == 0:
            ans += "b"
            B -= 1
            continue
        # a を先頭にする場合
        # A-1C(B-1) + A-1C(B-2) + ... + A-1C(0)
        # = A-1C(B-1) + A-1C(B-2) + ... + A-1C(A-1) + A-1C(A-2) + ... + A-1C(0)
        # = A-1C(B-1) + A-1C(A-1)
        # = A-1C(A-1) + A-1C(B-1)
        # = A-1C(B-1)
        # = A-1C(B-1) + A-1C(B-2) + ... + A-1C(0)
        # = A-1C(B-1) + A-1C(B-2) + ... + A-1C(A-1) + A-1C(A-2) + ... + A-1C(0)
        # = A-1C(A-1) + A-1C(B-1)
        # = A-1C(B-1)
        # = A-1C(B-1) + A-1C(B-2) + ... + A-1C(0)
        # = A-1C(B-1) + A-1C(B-2) + ... + A-1C(A-1) + A-1C(A-2) + ... + A-1C(0)
        # = A-1C(A-1) + A-1C(B-1)
        # = A-1C(B-1)
        # = A-1C(B-1) + A-1C(B-2) + ... + A-1C(0)
        # = A-1C(B-1) + A-1C(B-2) + ... + A-1C(A-1

if __name__ == '__main__':
    main()