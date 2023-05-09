def main():
    A, B, K = map(int, input().split())
    ans = ''
    while A > 0 or B > 0:
        if A == 0:
            ans += 'b'
            B -= 1
            continue
        if B == 0:
            ans += 'a'
            A -= 1
            continue
        if K > comb(A + B - 1, A - 1):
            ans += 'b'
            B -= 1
            K -= comb(A + B - 1, A - 1)
        else:
            ans += 'a'
            A -= 1
    print(ans)

if __name__ == '__main__':
    main()