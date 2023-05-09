def main():
    A,B,Q = map(int,input().split())
    s = [-10**10] + [int(input()) for _ in range(A)] + [10**10]
    t = [-10**10] + [int(input()) for _ in range(B)] + [10**10]
    x = [int(input()) for _ in range(Q)]
    for i in x:
        a = bisect.bisect_left(s,i)
        b = bisect.bisect_left(t,i)
        ans = 10**20
        for j in range(a-1,a+1):
            for k in range(b-1,b+1):
                ans = min(ans,abs(i-s[j])+abs(s[j]-t[k]),abs(i-t[k])+abs(t[k]-s[j]))
        print(ans)
import bisect
main()

if __name__ == '__main__':
    main()