Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, K = [int(x) for x in input().split()]
    P = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    ans = -10**10
    for i in range(N):
        tmp = 0
        now = i
        for j in range(K):
            now = P[now]-1
            tmp += C[now]
            if tmp <= 0:
                break
            if now == i:
                ans = max(ans, (K-j-1)//j*tmp+tmp)
                break
            ans = max(ans, tmp)
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10**18
    for i in range(N):
        total = 0
        cycle = [i]
        while P[cycle[-1]]-1 not in cycle:
            cycle.append(P[cycle[-1]]-1)
        for j in range(len(cycle)):
            total += C[cycle[j]]
            if total <= 0:
                continue
            temp = total*((K-j-1)//len(cycle))
            for k in range(K-j-1-(K-j-1)//len(cycle)*len(cycle)):
                temp += C[cycle[k]]
                ans = max(ans, temp)
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10**9
    for i in range(N):
        cycle = []
        j = i
        while True:
            cycle.append(C[j])
            j = P[j]-1
            if j == i:
                break
        cycle_sum = sum(cycle)
        cycle_len = len(cycle)
        cycle_max = max(cycle)
        if cycle_sum > 0:
            cycle_time = min(K//cycle_len, (K-cycle_len)//cycle_len+1)
            ans = max(ans, cycle_sum*cycle_time+cycle_max)
        else:
            cycle_time = min(K//cycle_len, (K-cycle_len)//cycle_len+1)
            ans = max(ans, cycle_sum*cycle_time)
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    score = 0
    for i in range(N):
        if P[i] != 0:
            j = i
            cycle = []
            while True:
                cycle.append(C[j])
                P[j], j = 0, P[j] - 1
                if j == i:
                    break
            cycle_sum = sum(cycle)
            cycle_len = len(cycle)
            max_cycle = 0
            for j in range(cycle_len):
                max_cycle = max(max_cycle, cycle[j])
                if j + 1 <= K:
                    max_cycle = max(max_cycle, cycle[j] + cycle_sum * ((K - j - 1) // cycle_len))
            score = max(score, max_cycle)
    print(score)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ans = -10**9

    for i in range(N):
        x = i
        score = 0
        path = []
        while True:
            x = P[x] - 1
            score += C[x]
            path.append(x)
            if x == i:
                break
        if score <= 0:
            ans = max(ans, max(C))
        else:
            cycle = len(path)
            loop = min(K // cycle, 2 * 10**5)
            score = score * loop
            ans = max(ans, score)
            for j in range(loop * cycle, K):
                x = P[x] - 1
                score += C[x]
                ans = max(ans, score)

    print(ans)

=======
Suggestion 6

def main():
    N,K=map(int,input().split())
    P=list(map(int,input().split()))
    C=list(map(int,input().split()))
    ans=-float('inf')
    for i in range(N):
        j=i
        score=0
        count=0
        while count<K:
            score+=C[P[j]-1]
            if score>ans:
                ans=score
            j=P[j]-1
            count+=1
            if j==i:
                break
        if count<K:
            loop=K//count
            score*=loop
            if score>ans:
                ans=score
            count+=loop*count
            while count<K:
                score+=C[P[j]-1]
                if score>ans:
                    ans=score
                j=P[j]-1
                count+=1
    print(ans)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # P[i] = P_i - 1
    for i in range(N):
        P[i] -= 1

    # C[i] = C_i
    # C[i] = C_{P_i}
    for i in range(N):
        C[i] = C[P[i]]

    # C[i] = C_{P_i} + C_{P_{P_i}} + ... + C_{P_{P_{P_{P_i}}}}
    for i in range(N):
        C[i] += C[P[i]]

    # C[i] = C_{P_i} + C_{P_{P_i}} + ... + C_{P_{P_{P_{P_i}}}} + C_{P_{P_{P_{P_{P_i}}}}}
    for i in range(N):
        C[i] += C[P[i]]

    # C[i] = C_{P_i} + C_{P_{P_i}} + ... + C_{P_{P_{P_{P_i}}}} + C_{P_{P_{P_{P_{P_i}}}}} + C_{P_{P_{P_{P_{P_{P_i}}}}}}
    for i in range(N):
        C[i] += C[P[i]]

    # C[i] = C_{P_i} + C_{P_{P_i}} + ... + C_{P_{P_{P_{P_i}}}} + C_{P_{P_{P_{P_{P_i}}}}} + C_{P_{P_{P_{P_{P_{P_i}}}}}} + C_{P_{P_{P_{P_{P_{P_{P_i}}}}}}}
    for i in range(N):
        C[i] += C[P[i]]

    # C[i] = C_{P_i} + C_{P_{P_i}} + ... + C_{P_{P_{P_{P_i}}}} + C_{P_{P_{P_{P_{P_i}}}}} + C_{P_{P_{P_{P_{P_{P_i}}}}}} + C_{P_{P_{P_{P_{P_{P_{P_i}}}}}}} + C_{P_{P_{P_{P_{

=======
Suggestion 8

def solve(N, K, P, C):
    res = -float("inf")
    for i in range(N):
        s = 0
        t = 0
        j = i
        while True:
            s += C[P[j]-1]
            t += 1
            j = P[j]-1
            if j == i:
                break
        if s > 0:
            if K >= t:
                res = max(res, s*((K-t)//t)+max(0, s))
            else:
                res = max(res, max(C[:t]))
        else:
            res = max(res, max(C[:t]))
    return res

=======
Suggestion 9

def solve(n, k, p, c):
    ans = -10**18
    for i in range(n):
        #print("i:", i)
        j = i
        s = 0
        m = 0
        while True:
            #print("j:", j)
            j = p[j] - 1
            s += c[j]
            m += 1
            if j == i:
                break
        if s > 0:
            #print("s:", s)
            #print("m:", m)
            t = (k - m) // m
            #print("t:", t)
            ans = max(ans, s * t + max(0, max(c[:j+1]) * (k - m - t * m)))
        else:
            ans = max(ans, max(c[:j+1]) * k)
    return ans
