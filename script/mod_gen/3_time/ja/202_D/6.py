def solve():
    A,B,K = map(int,input().split())
    ans = ""
    while A+B > 0:
        if A == 0:
            ans += "b"
            B -= 1
        elif B == 0:
            ans += "a"
            A -= 1
        else:
            if A >= B:
                if K <= A*B:
                    ans += "a"
                    A -= 1
                else:
                    ans += "b"
                    B -= 1
                    K -= A*B
            else:
                if K <= A*B:
                    ans += "b"
                    B -= 1
                else:
                    ans += "a"
                    A -= 1
                    K -= A*B
    print(ans)

if __name__ == '__main__':
    solve()