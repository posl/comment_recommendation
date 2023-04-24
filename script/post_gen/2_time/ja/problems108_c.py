Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    ans = 0
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if (a + b) % K == 0:
                ans += 1

    print(ans ** 3)

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    #N 以下の正の整数の組 (a,b,c) であって、a+b,b+c,c+a がすべて K の倍数であるようなものの個数を求めてください。
    #a+b,b+c,c+a がすべて K の倍数であるようなものの個数を求めてください。
    #a+b,b+c,c+a がすべて K の倍数であるようなものの個数を求めてください。
    #a+b,b+c,c+a がすべて K の倍数であるようなものの個数を求めてください。
    #a+b,b+c,c+a がすべて K の倍数であるようなものの個数を求めてください。
    #a+b,b+c,c+a がすべて K の倍数であるようなものの個数を求めてください。
    #a+b,b+c,c+a がすべて K の倍数であるようなものの個数を求めてください。
    #a+b,b+c,c+a がすべて K の倍数であるようなものの個数を求めてください。
    #a+b,b+c,c+a がすべて K の倍数であるようなものの個数を求めてください。
    #a+b,b+c,c+a がすべて K の倍数であるようなものの個数を求めてください。
    #a+b,b+c,c+a がすべて K の倍数であるようなものの個数を求めてください。
    #a+b,b+c,c+a がすべて K の倍数であるようなものの個数を求めてください。
    #a+b,b+c,c+a がすべて K の倍数であるようなものの個数を求めてください

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    a = [0] * k
    b = [0] * k
    c = [0] * k
    for i in range(1,n+1):
        a[i%k] += 1
        b[i%k] += 1
        c[i%k] += 1
    ans = 0
    for i in range(k):
        for j in range(k):
            for l in range(k):
                if (i+j+l)%k == 0:
                    ans += a[i]*b[j]*c[l]
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        ans += (N // i) * max(0, i - K + 1)
        ans += max(0, (N % i) - K + 1)
    print(ans)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    ans = 0
    for a in range(1, N + 1):
        b = c = a
        if (a + b) % K == 0 and (b + c) % K == 0 and (c + a) % K == 0:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N,K = map(int, input().split())
    a = []
    b = []
    c = []
    for i in range(1,N+1):
        if i%K == 0:
            a.append(i)
        elif i%K == K/2:
            b.append(i)
        else:
            c.append(i)
    print(len(a)**3 + len(b)**3 + len(c)**3 - len(b)*len(c)*len(a)*3)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        ans += (N//i) * (i//K)
        if i%K == 0:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n,k=map(int,input().split())
    ans=0
    for a in range(1,n+1):
        if a%k==0:
            ans+=n**3
        else:
            for b in range(1,n+1):
                if (a+b)%k==0:
                    ans+=n**2
                else:
                    for c in range(1,n+1):
                        if (a+b+c)%k==0:
                            ans+=n
    print(ans)

main()

=======
Suggestion 9

def main():
    #入力
    N, K = map(int, input().split())
    #出力
    print(N//K**3)
