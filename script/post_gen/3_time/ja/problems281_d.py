Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(N):
        for j in range(i+1, N):
            S.add(A[i] + A[j])
    ans = -1
    for i in S:
        if i % D == 0:
            ans = max(ans, i)
    print(ans)

=======
Suggestion 2

def main():
    N,K,D = map(int,input().split())
    A = list(map(int,input().split()))
    S = set()
    for i in range(N):
        for j in range(i+1,N):
            S.add(A[i]+A[j])
    S = sorted(list(S))
    for i in range(len(S)-1,-1,-1):
        if S[i] % D == 0:
            print(S[i])
            return
    print(-1)

=======
Suggestion 3

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    S = set()
    for i in range(K):
        for j in range(i+1, K):
            S.add(A[i]+A[j])
    S = sorted(list(S), reverse=True)
    for s in S:
        if s % D == 0:
            print(s)
            return
    print(-1)

=======
Suggestion 4

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    #A = [1, 2, 3, 4]
    #N = 4
    #K = 2
    #D = 2
    #A = [1, 3, 5]
    #N = 3
    #K = 1
    #D = 2
    #A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #N = 10
    #K = 3
    #D = 3
    #A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #N = 10
    #K = 3
    #D = 4
    #A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #N = 10
    #K = 3
    #D = 5
    #A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #N = 10
    #K = 3
    #D = 6
    #A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #N = 10
    #K = 3
    #D = 7
    #A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #N = 10
    #K = 3
    #D = 8
    #A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #N = 10
    #K = 3
    #D = 9
    #A = [1, 2, 3, 4,

=======
Suggestion 5

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    S = [0]
    for i in range(N):
        S.append(S[i]+A[i])
    if S[K] < D:
        print(-1)
    else:
        print(S[K]//D*D)

=======
Suggestion 6

def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    # A = [1, 2, 3, 4]
    # K = 2
    # D = 2
    # N = 4

    A.sort(reverse=True)
    # A = [4, 3, 2, 1]
    ans = 0
    for i in range(K):
        ans += A[i]
    # ans = 7

    if ans % D == 0:
        print(ans)
    else:
        print(-1)

main()

=======
Suggestion 7

def main():
    N, K, D = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    #print(N, K, D, a)
    if K == 1:
        if a[0] % D == 0:
            print(a[0])
        else:
            print(-1)
    elif K == N:
        if a[-1] % D == 0:
            print(a[-1])
        else:
            print(-1)
    else:
        #a[0]からa[N-1]までの間にDの倍数があるかどうか
        if a[0] % D == 0 or a[-1] % D == 0:
            print(a[-1])
        else:
            #a[0]からa[N-1]までの間にDの倍数があるかどうか
            if a[0] // D == a[-1] // D:
                print(-1)
            else:
                #a[0]からa[N-1]までの間にDの倍数があるかどうか
                if a[0] // D == a[-1] // D - 1:
                    if (a[-1] - a[0]) % D == 0:
                        print(-1)
                    else:
                        print(a[-1])
                else:
                    #a[0]からa[N-1]までの間にDの倍数があるかどうか
                    if a[0] // D == a[-1] // D - 2:
                        if (a[-1] - a[0]) % D == 0:
                            print(-1)
                        else:
                            print(a[-1])
                    else:
                        print(-1)

=======
Suggestion 8

def main():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    # print(a)
    s = set()
    for i in range(n):
        for j in range(i+1,n):
            s.add(a[i]+a[j])
    # print(s)
    s = list(s)
    s.sort()
    # print(s)
    for i in range(len(s)-1,-1,-1):
        if s[i]%d == 0:
            print(s[i])
            return
    print(-1)

=======
Suggestion 9

def main():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    #print(n,k,d,a)
    a.sort(reverse=True)
    #print(a)
    ans = -1
    for i in range(2**n):
        s = 0
        for j in range(n):
            if (i >> j) & 1:
                s += a[j]
        #print(i,s)
        if s % d == 0:
            ans = max(ans,s)
    print(ans)

=======
Suggestion 10

def main():
    #input
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    #compute
    #output
    if K*D>N:
        print(-1)
    else:
        print(D*(sum(A[:K*D])-sum(A[:K*(D-1)])))
    return
