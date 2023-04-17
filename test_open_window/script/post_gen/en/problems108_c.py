Synthesizing 10/10 solutions

=======

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if i + j + k == K * (i // K + j // K + k // K):
                    ans += 1
    print(ans)

=======

def main():
    n, k = map(int, input().split())
    ans = 0
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                if (a + b) % k == 0 and (b + c) % k == 0 and (c + a) % k == 0:
                    ans += 1
    print(ans)

main()

=======

def main():
    n, k = map(int, input().split())
    ans = 0
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if (a + b) % k == 0:
                for c in range(1, n + 1):
                    if (b + c) % k == 0 and (c + a) % k == 0:
                        ans += 1
    print(ans)

=======

def main():
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        if i % K == 0:
            ans += 1
    print(ans**3)

=======

def   main (): 
     N ,   K   =   map ( int ,   input (). split ()) 

     if   K   %   2   ==   0 : 
         K2   =   K   //   2 
         cnt   =   ( N   //   K )   **   3   +   ( N   //   K2   -   N   //   K )   **   3 
     else : 
         cnt   =   ( N   //   K )   **   3 

     print ( cnt )

=======

def main():
    N,K = map(int,input().split())
    print(N//K * N//K * N//K + (N//K + 1)**3 if K%2 == 0 else N//K * N//K * N//K)

=======

def main():
    N, K = map(int, input().split())

    if N >= K:
        n = N // K
        ans = n ** 3
        if K % 2 == 0:
            n1 = (N + K // 2) // K
            ans += n1 ** 3
    else:
        ans = 0
    print(ans)

=======

def   main ():
    N,K  =  map ( int ,input().split())
    ans  =  0
    for  i  in   range ( 1 ,N+1):
        for  j  in   range ( 1 ,N+1):
            for  k  in   range ( 1 ,N+1):
                if  (i+j)%K== 0  and  (j+k)%K== 0  and  (k+i)%K== 0 :
                   ans  +=  1 
    print(ans)

=======

def main():
    N, K = map(int, input().split())

    # a+b,b+c,c+aがすべてKの倍数
    # a+bはKの倍数
    # b+cはKの倍数
    # c+aはKの倍数
    # a+b=b+c=c+a
    # a=b=c

    # a,b,cは全てKの倍数
    # a,b,cの最大値はN
    # a,b,cの最小値はK
    # a,b,cは全てKの倍数なので、Kで割った余りはK-1以下

    # aの最大値はN
    # aの最小値はK
    # bの最大値はN
    # bの最小値はK
    # cの最大値はN
    # cの最小値はK

    # a,b,cの最大値はN
    # a,b,cの最小値はK
    # a+bの最大値はN+N
    # a+bの最小値はK+K
    # b+cの最大値はN+N
    # b+cの最小値はK+K
    # c+aの最大値はN+N
    # c+aの最小値はK+K

    # a+b,b+c,c+aがすべてKの倍数
    # a+b,b+c,c+aがすべてKの倍数の場合
    # a+bはKの倍数
    # b+cはKの倍数
    # c+aはKの倍数

    # a+b,b+c,c+aがすべてKの倍数
    # a+b,b+c,c+aがすべてKの倍数の場合
    # a+bはKの倍数
    # b+cはKの倍数
    # c+aはKの倍数

    # a+b,b+c,c+aがすべてKの倍数
    # a+b,b+c,c+aがすべてKの倍数の場合
    # a+b

=======

def count_triples(n,k):
    return (n//k)**3
