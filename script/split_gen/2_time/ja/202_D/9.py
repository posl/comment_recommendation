def main():
    A,B,K = map(int,input().split())
    ans = ''
    while A and B:
        if A*B < K:
            K -= A*B
            if A > B:
                ans += 'b'
                B -= 1
            else:
                ans += 'a'
                A -= 1
        else:
            if A > B:
                ans += 'a'
                A -= 1
            else:
                ans += 'b'
                B -= 1
    while A:
        ans += 'a'
        A -= 1
    while B:
        ans += 'b'
        B -= 1
    print(ans)
