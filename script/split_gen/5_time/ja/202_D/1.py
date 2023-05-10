def main():
    A,B,K = map(int,input().split())
    S = A+B
    ans = ""
    for i in range(S):
        if A == 0:
            ans += "b"
            B -= 1
            continue
        if B == 0:
            ans += "a"
            A -= 1
            continue
        n = 1
        for j in range(A+B-1):
            n *= (A+B-j)
            n //= (j+1)
        if K <= n:
            ans += "a"
            A -= 1
        else:
            ans += "b"
            K -= n
            B -= 1
    print(ans)
