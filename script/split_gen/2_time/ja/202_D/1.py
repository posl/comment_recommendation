def main():
    A,B,K = map(int,input().split())
    ans = ""
    while A > 0 or B > 0:
        if A == 0:
            ans += "b"
            B -= 1
        elif B == 0:
            ans += "a"
            A -= 1
        else:
            tmp = 1
            for i in range(1,A+B):
                tmp *= i
                if i == A:
                    tmp //= i
                    tmp //= B
            if K <= tmp:
                ans += "a"
                A -= 1
            else:
                ans += "b"
                B -= 1
                K -= tmp
    print(ans)
