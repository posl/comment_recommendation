Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    C = list(map(int,input().split()))
    score = []
    for i in range(N):
        #print('i',i)
        #print('P[i]',P[i])
        #print('C[i]',C[i])
        #print('P[P[i]-1]',P[P[i]-1])
        #print('C[P[i]-1]',C[P[i]-1])
        #print('P[P[P[i]-1]-1]',P[P[P[i]-1]-1])
        #print('C[P[P[i]-1]-1]',C[P[P[i]-1]-1])
        #print('P[P[P[P[i]-1]-1]-1]',P[P[P[P[i]-1]-1]-1])
        #print('C[P[P[P[i]-1]-1]-1]',C[P[P[P[i]-1]-1]-1])
        #print('P[P[P[P[P[i]-1]-1]-1]-1]',P[P[P[P[P[i]-1]-1]-1]-1])
        #print('C[P[P[P[P[i]-1]-1]-1]-1]',C[P[P[P[P[i]-1]-1]-1]-1])
        #print('P[P[P[P[P[P[i]-1]-1]-1]-1]-1]',P[P[P[P[P[P[i]-1]-1]-1]-1]-1])
        #print('C[P[P[P[P[P[i]-1]-1]-1]-1]-1]',C[P[P[P[P[P[i]-1]-1]-1]-1]-1])
        #print('P[P[P[P[P[P[P[i]-1]-1]-1]-1]-1]-1]',P[P[P[P[P[P[P[i]-1]-1]-1]-1]-1]-1])
        #print('C[P[P[P[P[P[P[i]-1]-1]-1]-1]-1]-1]',C[P[P[P[P[P[P[i]-1]-1]-1]-1]-1]-1])
        #print('P[P[P[P[P[P[P[P[i]-1]-1]-1]-1]-1]-1]-1]',P[P[P[P[P[P[P[i]-1]-1]-1]-1]-1]-1]-1])
        #print('C[P

=======
Suggestion 3

def get_max_score(n, k, p_list, c_list):
    # 从某个方格开始，最多走k步后的最大分数
    max_score = -1000000000000000
    for i in range(0, n):
        # 从第i个方格开始
        score = 0
        # 第一步
        score += c_list[p_list[i]-1]
        # 第二步
        score += c_list[p_list[p_list[i]-1]-1]
        if score > max_score:
            max_score = score
        # 第三步
        score += c_list[p_list[p_list[p_list[i]-1]-1]-1]
        if score > max_score:
            max_score = score
    return max_score

=======
Suggestion 4

def solve():
    pass

=======
Suggestion 5

def solution():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -float('inf')
    for i in range(N):
        score = 0
        pos = i
        cnt = 0
        while cnt < K:
            pos = P[pos] - 1
            score += C[pos]
            cnt += 1
            ans = max(ans, score)
            if pos == i:
                if K % cnt == 0:
                    break
                else:
                    score = score * (K // cnt - 1)
                    cnt = K // cnt * cnt
    print(ans)

=======
Suggestion 6

def max_score(n, k, p, c):
    max_score = -1000000000
    for i in range(n):
        score = 0
        step = 0
        next = i
        while step < k:
            next = p[next] - 1
            score += c[next]
            if score > max_score:
                max_score = score
            step += 1
            if next == i:
                break
    return max_score

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    p = [i - 1 for i in p]
    ans = -10 ** 18
    for i in range(n):
        x = i
        s = 0
        l = 0
        while True:
            x = p[x]
            s += c[x]
            l += 1
            if x == i:
                break
        t = 0
        x = i
        while True:
            x = p[x]
            t += c[x]
            l -= 1
            if l == k:
                break
        if s > 0:
            if t > 0:
                u = (k // l - 1) * l
                for j in range(l):
                    x = p[x]
                    t += c[x]
                    if t > ans:
                        ans = t
                for j in range(l):
                    x = p[x]
                    t += c[x]
                    u += 1
                    if t > ans:
                        ans = t
                    if u == k:
                        break
            else:
                for j in range(k):
                    x = p[x]
                    t += c[x]
                    if t > ans:
                        ans = t
        else:
            for j in range(k):
                x = p[x]
                t += c[x]
                if t > ans:
                    ans = t
    print(ans)
