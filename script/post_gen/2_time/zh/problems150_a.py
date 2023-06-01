Synthesizing 10/10 solutions

=======
Suggestion 1

def get_max_score(N, K, R, S, P, T):
    score = 0
    for i in range(N):
        if T[i] == 'r':
            score += R
        elif T[i] == 's':
            score += S
        elif T[i] == 'p':
            score += P
    return score

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    score = 0
    for i in range(n):
        if t[i] == 'r':
            if i >= k and t[i-k] == 'r':
                score += 0
            else:
                score += p
        elif t[i] == 's':
            if i >= k and t[i-k] == 's':
                score += 0
            else:
                score += r
        elif t[i] == 'p':
            if i >= k and t[i-k] == 'p':
                score += 0
            else:
                score += s
    print(score)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    #print(n,k,r,s,p,t)
    #print(r,s,p)
    #print(t)
    score = 0
    for i in range(n):
        if t[i] == 'r':
            score += p
        elif t[i] == 's':
            score += r
        else:
            score += s
    for i in range(n-k):
        if t[i] == 'r' and t[i+k] == 'r':
            score -= p
        elif t[i] == 's' and t[i+k] == 's':
            score -= r
        elif t[i] == 'p' and t[i+k] == 'p':
            score -= s
    print(score)

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    score = 0
    for i in range(n):
        if i >= k and t[i] == t[i-k] and t[i] == 'r':
            t = t[:i] + 'p' + t[i+1:]
        elif i >= k and t[i] == t[i-k] and t[i] == 's':
            t = t[:i] + 'r' + t[i+1:]
        elif i >= k and t[i] == t[i-k] and t[i] == 'p':
            t = t[:i] + 's' + t[i+1:]
        if t[i] == 'r':
            score += p
        elif t[i] == 's':
            score += r
        elif t[i] == 'p':
            score += s
    print(score)

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    #print(N, K, R, S, P, T)
    #dp[i][j]表示前i轮，第i轮使用了j手的最大得分
    #第i轮使用了j手，第i-1轮使用了k手，k!=j, k属于[1, 2, 3]，取最大值
    #dp[i][j] = max(dp[i-1][k] + score(i, j))
    #dp[0][j] = 0
    #score(i, j)表示第i轮使用了j手的得分
    #score(i, j) = R if j == 1
    #score(i, j) = S if j == 2
    #score(i, j) = P if j == 3
    #score(i, j) = 0 if j == 0
    dp = [[0 for _ in range(4)] for _ in range(N+1)]
    score = [0, R, S, P]
    for i in range(1, N+1):
        for j in range(1, 4):
            dp[i][j] = max(dp[i-1][k] + score[j] for k in range(1, 4) if k != j)
        if T[i-1] == 'r':
            dp[i][1] = max(dp[i][1], dp[i-1][0] + score[1])
        elif T[i-1] == 's':
            dp[i][2] = max(dp[i][2], dp[i-1][0] + score[2])
        elif T[i-1] == 'p':
            dp[i][3] = max(dp[i][3], dp[i-1][0] + score[3])
    ans = max(dp[N][1], dp[N][2], dp[N][3])
    print(ans)
    return 0

solve()

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    R,S,P = map(int,input().split())
    T = input()
    #print(N,K,R,S,P,T)
    # N,K,R,S,P,T = 5,2,8,7,6,"rsrpr"
    # N,K,R,S,P,T = 7,1,100,10,1,"ssssppr"
    # N,K,R,S,P,T = 30,5,325,234,123,"rspsspspsrpspsppprpsprpspsppprpr"
    # N,K,R,S,P,T = 30,5,325,234,123,"rspsspspsrpspsppprpsprpspsppprpr"
    # N,K,R,S,P,T = 30,5,325,234,123,"rspsspspsrpspsppprpsprpspsppprpr"
    # N,K,R,S,P,T = 30,5,325,234,123,"rspsspspsrpspsppprpsprpspsppprpr"
    # N,K,R,S,P,T = 30,5,325,234,123,"rspsspspsrpspsppprpsprpspsppprpr"
    # N,K,R,S,P,T = 30,5,325,234,123,"rspsspspsrpspsppprpsprpspsppprpr"
    # N,K,R,S,P,T = 30,5,325,234,123,"rspsspspsrpspsppprpsprpspsppprpr"
    # N,K,R,S,P,T = 30,5,325,234,123,"rspsspspsrpspsppprpsprpspsppprpr"

    # N,K,R,S,P,T = 30,5,325,234,123,"rspsspspsrpspsppprpsprpspsppprpr"
    # N,K,R,S,P,T = 30,5,325,234,123,"rspsspspsrpspsppprpsprpspsppprpr"

    # N,K,R,S,P,T = 30,5,325,234,123,"rspsspspsrpspsppprpsprpspsppprpr"

    # N,K,R,S

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()
    #print(N, K, R, S, P, T)
    #N, K, R, S, P = 5, 2, 8, 7, 6
    #T = 'rsrpr'
    #N, K, R, S, P = 7, 1, 100, 10, 1
    #T = 'ssssppr'
    #N, K, R, S, P = 30, 5, 325, 234, 123
    #T = 'rspsspspsrpspsppprpsprpspsppprpr'
    #print(N, K, R, S, P, T)
    #print(len(T))
    #print(T[0])
    #print(T[1])
    #print(T[2])
    #print(T[3])
    #print(T[4])
    #print(T[5])
    #print(T[6])
    #print(T[7])
    #print(T[8])
    #print(T[9])
    #print(T[10])
    #print(T[11])
    #print(T[12])
    #print(T[13])
    #print(T[14])
    #print(T[15])
    #print(T[16])
    #print(T[17])
    #print(T[18])
    #print(T[19])
    #print(T[20])
    #print(T[21])
    #print(T[22])
    #print(T[23])
    #print(T[24])
    #print(T[25])
    #print(T[26])
    #print(T[27])
    #print(T[28])
    #print(T[29])
    #print(T[30])
    #print(T[31])
    #print(T[32])
    #print(T[33])
    #print(T[34])
    #print(T[35])
    #print(T[36])
    #print(T[37])
    #print(T[38])
    #print(T[39])
    #print(T[40])
    #print(T[41])
    #print(T[42])
    #print(T[43])

=======
Suggestion 8

def main():
    # N,K = map(int,input().split(" "))
    # R,S,P = map(int,input().split(" "))
    # T = input()
    N,K = 5,2
    R,S,P = 8,7,6
    T = "rsrpr"
    # N,K = 7,1
    # R,S,P = 100,10,1
    # T = "ssssppr"
    # N,K = 30,5
    # R,S,P = 325,234,123
    # T = "rspsspspsrpspsppprpsprpspsppprpr"
    result = 0
    for i in range(N):
        if i < K:
            if T[i] == "r":
                result += P
            elif T[i] == "s":
                result += R
            else:
                result += S
        else:
            if T[i] == "r":
                if T[i-K] == "r":
                    if R <= P:
                        result += P
                    else:
                        result += R
                elif T[i-K] == "s":
                    result += P
                else:
                    result += R
            elif T[i] == "s":
                if T[i - K] == "r":
                    result += R
                elif T[i - K] == "s":
                    if S <= R:
                        result += R
                    else:
                        result += S
                else:
                    result += S
            else:
                if T[i - K] == "r":
                    result += P
                elif T[i - K] == "s":
                    result += S
                else:
                    if P <= S:
                        result += S
                    else:
                        result += P
    print(result)

=======
Suggestion 9

def get_score(s):
    if s == 'r':
        return R
    elif s == 's':
        return S
    else:
        return P

N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

score = 0
for i in range(N):
    if i >= K and T[i] == T[i-K] and T[i] == T[i-K]:
        continue
    score += get_score(T[i])

print(score)

=======
Suggestion 10

def get_max_score(n, k, r, s, p, t):
    #print(n, k, r, s, p, t)
    sum = 0
    for i in range(n):
        if t[i] == 'r':
            sum += p
        elif t[i] == 's':
            sum += r
        elif t[i] == 'p':
            sum += s
    #print("sum=", sum)

    for i in range(k):
        if t[i] == t[i+k]:
            if i+k+k < n:
                if t[i+k+k] == 'r':
                    sum -= p
                elif t[i+k+k] == 's':
                    sum -= r
                elif t[i+k+k] == 'p':
                    sum -= s
            else:
                sum -= 0

    return sum
