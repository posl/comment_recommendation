Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    C = list(map(int, input().split()))
    mod = 10**9+7
    ans = 1
    for i in range(N):
        if i == 0:
            ans *= C[i]
            ans %= mod
            continue
        if C[i] == C[i-1]:
            ans *= C[i] - 1
            ans %= mod
            continue
        if C[i] < C[i-1]:
            ans *= 0
            ans %= mod
            continue
        if C[i] > C[i-1]:
            ans *= C[i] - 1
            ans %= mod
            continue
    print(ans)

=======
Suggestion 2

def main():
    import sys
    input = sys.stdin.readline
    mod = 10**9 + 7
    N = int(input())
    C = list(map(int, input().split()))
    if C[0] == 1:
        ans = 1
    else:
        ans = 0
    for i in range(1, N):
        if C[i] < C[i-1]:
            ans = 0
            break
        elif C[i] == C[i-1]:
            ans *= 2
        elif C[i] - C[i-1] == 1:
            ans *= C[i-1]
        else:
            ans *= C[i-1] * (C[i] - C[i-1] + 1)
        ans %= mod
    print(ans)

=======
Suggestion 3

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    C = list(map(int, input().split()))
    MOD = 10**9+7
    ans = 1
    for i in range(N-1):
        if C[i] < C[i+1]:
            ans *= 1
        elif C[i] > C[i+1]:
            ans *= 0
        else:
            ans *= 2
        ans %= MOD
    print(ans)

=======
Suggestion 4

def main():
    MOD = 10**9 + 7
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        if c[i] < i + 1:
            print(0)
            return
        ans = ans * (c[i] - i) % MOD
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    C = list(map(int, input().split()))
    MOD = 10**9 + 7
    A = [0] * (N+1)
    A[0] = 1
    for i in range(N):
        A[i+1] = A[i] * (C[i] - i)
        A[i+1] %= MOD
    print(A[N])

main()

=======
Suggestion 6

def main():
    N = int(input())
    C = list(map(int, input().split()))
    MOD = 10**9 + 7
    ans = 1
    for i in range(N):
        ans *= min(C[i] - i, N)
        ans %= MOD
    print(ans)

=======
Suggestion 7

def main():
    N=int(input())
    C=list(map(int,input().split()))
    MOD=10**9+7
    ans=1
    for i in range(N):
        if i==0:
            ans*=C[i]
        else:
            ans*=max(0,C[i]-i)
            ans%=MOD
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    C = list(map(int, input().split()))

    mod = 10 ** 9 + 7
    ans = 1
    prev = 0
    for i in range(N):
        if prev == C[i]:
            ans = ans * (C[i] - 1) % mod
        elif prev + 1 == C[i]:
            ans = ans * C[i] % mod
        elif prev < C[i]:
            ans = ans * C[i] * (C[i] - 1) // 2 % mod
        else:
            ans = 0
        prev = C[i]
    print(ans)

=======
Suggestion 9

def main():
    #input
    N = int(input())
    Cs = list(map(int, input().split()))
    MOD = 10**9+7

    #compute
    if Cs[0] == 1:
        ans = 1
    else:
        ans = 0
    for i in range(1, N):
        ans *= Cs[i-1]-Cs[i]+1
        ans %= MOD
        if Cs[i] < Cs[i-1]:
            ans *= pow(Cs[i-1]-Cs[i]+1, MOD-2, MOD)
            ans %= MOD
        elif Cs[i] > Cs[i-1]+1:
            ans = 0
            break

    #output
    print(ans)

=======
Suggestion 10

def main():
    #input
    N = int(input())
    Cs = list(map(int, input().split()))
    #count
    if N == 1:
        print(1)
        return
    if N == 2:
        if Cs[0] == Cs[1]:
            print(1)
        else:
            print(2)
        return
    mod = 10**9+7
    ans = 1
    for i in range(1,N):
        if Cs[i-1] != Cs[i]:
            ans *= 2
            ans %= mod
        else:
            if Cs[i-1] == 1 and Cs[i] == 1:
                print(0)
                return
            elif Cs[i-1] == 1 and Cs[i] != 1:
                ans *= 1
                ans %= mod
            elif Cs[i-1] != 1 and Cs[i] == 1:
                ans *= 1
                ans %= mod
            else:
                ans *= 1
                ans %= mod
    print(ans)
