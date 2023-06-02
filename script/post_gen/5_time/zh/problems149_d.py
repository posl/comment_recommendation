Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()

    #rps = [r,s,p]
    #t = [r,s,p]
    #t.sort(reverse=True)
    #pri

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    R,S,P = map(int,input().split())
    T = input()
    #print(N,K,R,S,P,T)
    #print(len(T))
    #print(T[0:K])
    #print(T[K:])

    #print(T[K:]+T[0:K])
    #print(T[K:]+T[0:K][0:K])
    #print(T[K:]+T[0:K][0:K][0:K])
    #print(T[K:]+T[0:K][0:K][0:K][0:K])
    #print(T[K:]+T[0:K][0:K][0:K][0:K][0:K])
    #print(T[K:]+T[0:K][0:K][0:K][0:K][0:K][0:K])
    #print(T[K:]+T[0:K][0:K][0:K][0:K][0:K][0:K][0:K])

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    # print(n, k, r, s, p, t)
    score = 0
    for i in range(n):
        if t[i] == 'r':
            score += p
        elif t[i] == 's':
            score += r
        else:
            score += s
    print(score)
    return 0

=======
Suggestion 4

def problems149_d():
    return None

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    point = 0
    for i in range(n):
        if t[i] == "r":
            if i < k:
                point += p
            elif t[i-k] == "p":
                t = t[:i] + " " + t[i+1:]
            else:
                point += p
        elif t[i] == "s":
            if i < k:
                point += r
            elif t[i-k] == "r":
                t = t[:i] + " " + t[i+1:]
            else:
                point += r
        else:
            if i < k:
                point += s
            elif t[i-k] == "s":
                t = t[:i] + " " + t[i+1:]
            else:
                point += s
    print(point)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = input()
    ans = 0
    for i in range(n):
        if i < k:
            if t[i] == 'r':
                ans += p
            elif t[i] == 's':
                ans += r
            else:
                ans += s
        else:
            if t[i] == 'r':
                if t[i - k] == 'r':
                    t = t[:i] + 'x' + t[i + 1:]
                else:
                    ans += p
            elif t[i] == 's':
                if t[i - k] == 's':
                    t = t[:i] + 'x' + t[i + 1:]
                else:
                    ans += r
            else:
                if t[i - k] == 'p':
                    t = t[:i] + 'x' + t[i + 1:]
                else:
                    ans += s
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    score = 0
    for i in range(N):
        if i < K:
            if T[i] == "r":
                score += P
            elif T[i] == "s":
                score += R
            else:
                score += S
        else:
            if T[i] == T[i - K]:
                T[i] = "x"
            elif T[i] == "r":
                score += P
            elif T[i] == "s":
                score += R
            else:
                score += S
    print(score)

=======
Suggestion 8

def problems149_d():
    pass

=======
Suggestion 9

def main():
    N,K=map(int,input().split())
    R,S,P=map(int,input().split())
    T=input()
    score=0
    for i in range(N):
        if T[i]=='r':
            if i-K>=0 and T[i-K]=='p':
                T[i]='x'
            else:
                score+=R
        elif T[i]=='s':
            if i-K>=0 and T[i-K]=='r':
                T[i]='x'
            else:
                score+=S
        elif T[i]=='p':
            if i-K>=0 and T[i-K]=='s':
                T[i]='x'
            else:
                score+=P
    print(score)
