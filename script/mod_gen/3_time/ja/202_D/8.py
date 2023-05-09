def main():
    A, B, K = map(int, input().split())
    ans = ''
    while A > 0 and B > 0:
        if A > B:
            if K <= A:
                ans += 'a'
                A -= 1
            else:
                ans += 'b'
                K -= A
                B -= 1
        else:
            if K <= B:
                ans += 'b'
                B -= 1
            else:
                ans += 'a'
                K -= B
                A -= 1
    while A > 0:
        ans += 'a'
        A -= 1
    while B > 0:
        ans += 'b'
        B -= 1
    print(ans)

if __name__ == '__main__':
    main()