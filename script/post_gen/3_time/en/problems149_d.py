Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    ans = 0
    for i in range(N):
        if i < K:
            if T[i] == "r":
                ans += P
            elif T[i] == "s":
                ans += R
            else:
                ans += S
        else:
            if T[i] == "r":
                if T[i-K] != "r":
                    ans += P
            elif T[i] == "s":
                if T[i-K] != "s":
                    ans += R
            else:
                if T[i-K] != "p":
                    ans += S
    print(ans)

=======
Suggestion 2

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
            if t[i] == 'r' and t[i-k] != 'p':
                ans += p
                t = t[:i] + 'p' + t[i+1:]
            elif t[i] == 's' and t[i-k] != 'r':
                ans += r
                t = t[:i] + 'r' + t[i+1:]
            elif t[i] == 'p' and t[i-k] != 's':
                ans += s
                t = t[:i] + 's' + t[i+1:]

    print(ans)

=======
Suggestion 3

def main():
    N,K = map(int,input().split())
    R,S,P = map(int,input().split())
    T = input()
    ans = 0
    for i in range(N):
        if i < K:
            if T[i] == 'r':
                ans += P
            elif T[i] == 's':
                ans += R
            elif T[i] == 'p':
                ans += S
        else:
            if T[i] == 'r' and T[i-K] != 'p':
                ans += P
            elif T[i] == 's' and T[i-K] != 'r':
                ans += R
            elif T[i] == 'p' and T[i-K] != 's':
                ans += S
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    T = list(T)
    for i in range(N):
        if T[i] == 'r':
            T[i] = P
        elif T[i] == 's':
            T[i] = R
        else:
            T[i] = S
    for i in range(K, N):
        if T[i] == T[i-K]:
            T[i] = 0
    print(sum(T))

=======
Suggestion 5

def rps_battle(N,K,R,S,P,T):
    #N = int(input())
    #K = int(input())
    #R = int(input())
    #S = int(input())
    #P = int(input())
    #T = input()
    score = 0
    for i in range(N):
        if i < K:
            if T[i] == 'r':
                score += P
            elif T[i] == 's':
                score += R
            elif T[i] == 'p':
                score += S
        else:
            if T[i] == T[i-K]:
                T = T[:i]+'X'+T[i+1:]
            else:
                if T[i] == 'r':
                    score += P
                elif T[i] == 's':
                    score += R
                elif T[i] == 'p':
                    score += S
    return score

=======
Suggestion 6

def calc_score(T, N, K, R, S, P):
    score = 0
    for i in range(N):
        if T[i] == 'r':
            score += P
        elif T[i] == 's':
            score += R
        elif T[i] == 'p':
            score += S
        if i >= K:
            if T[i] == T[i-K]:
                T[i] = ' '
    return score

=======
Suggestion 7

def main():
    # Read input
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()

    # Initialize
    score = 0
    prev = [None]*K

    # Play
    for i in range(N):
        # Get score
        if T[i] == "r":
            score += P
            prev[i%K] = "p"
        elif T[i] == "s":
            score += R
            prev[i%K] = "r"
        elif T[i] == "p":
            score += S
            prev[i%K] = "s"

        # Check previous hand
        if i >= K and prev[i%K] == prev[(i-K)%K]:
            score -= R if prev[i%K] == "r" else (S if prev[i%K] == "s" else P)
            prev[i%K] = None

    # Output
    print(score)

=======
Suggestion 8

def main():
    #read input
    n,k=map(int,input().split())
    r,s,p=map(int,input().split())
    t=input()
    #initialize variables
    ans=0
    #process
    for i in range(n):
        if i-k>=0 and t[i]==t[i-k]:
            t=t[:i]+'x'+t[i+1:]
        if t[i]=='r':
            ans+=p
        elif t[i]=='s':
            ans+=r
        elif t[i]=='p':
            ans+=s
    #print answer
    print(ans)

main()

=======
Suggestion 9

def main():
    N, K = list(map(int, input().split()))
    R, S, P = list(map(int, input().split()))
    T = input()
    
    #dp[i] = max score if we play the i-th hand
    #dp[i] = max(dp[i-K] + score if we play the i-th hand, dp[i-1])
    dp = [0] * N
    for i in range(N):
        if i < K:
            if T[i] == 'r':
                dp[i] = P
            elif T[i] == 's':
                dp[i] = R
            else:
                dp[i] = S
        else:
            if T[i] == 'r':
                dp[i] = max(dp[i-K] + P, dp[i-1])
            elif T[i] == 's':
                dp[i] = max(dp[i-K] + R, dp[i-1])
            else:
                dp[i] = max(dp[i-K] + S, dp[i-1])
    print(dp[-1])

=======
Suggestion 10

def RPS_Battle(N,K,R,S,P,T):
    #N: number of rounds
    #K: number of rounds that cannot be used the same hand
    #R: point for winning with Rock
    #S: point for winning with Scissors
    #P: point for winning with Paper
    #T: string of hands that the machine will play in each round
    #return: maximum total score earned in the game
    
    score = 0
    for i in range(N):
        if i < K:
            if T[i] == 'r':
                score += P
            elif T[i] == 's':
                score += R
            else:
                score += S
        else:
            if T[i-K] == T[i]:
                T = T[:i] + 'x' + T[i+1:]
            else:
                if T[i] == 'r':
                    score += P
                elif T[i] == 's':
                    score += R
                else:
                    score += S
    return score
