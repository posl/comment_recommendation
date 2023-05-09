def main():
    A,B,Q = map(int,input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]
    for x in X:
        if x < S[0]:
            print(S[0]-x+min(S[0]-x,T[0]-S[0]))
        elif x > T[-1]:
            print(x-T[-1]+min(x-T[-1],T[-1]-S[-1]))
        else:
            l = 0
            r = A-1
            while r-l > 1:
                m = (l+r)//2
                if S[m] >= x:
                    r = m
                else:
                    l = m
            s = r
            l = 0
            r = B-1
            while r-l > 1:
                m = (l+r)//2
                if T[m] >= x:
                    r = m
                else:
                    l = m
            t = r
            ans = min(S[s]-x,T[t]-x)
            ans += min(S[s]-x,x-T[t])
            ans += min(x-S[s],T[t]-x)
            ans += min(x-S[s],x-T[t])
            print(ans)
