Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    pass

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))

    visited = [False] * N
    cycles = []
    for i in range(N):
        if visited[i]:
            continue
        cycle = []
        j = i
        while not visited[j]:
            visited[j] = True
            cycle.append(C[P[j]-1])
            j = P[j]-1
        cycles.append(cycle)

    ans = -10**18
    for cycle in cycles:
        cycle.sort(reverse=True)
        s = sum(cycle)
        t = 0
        for i in range(len(cycle)):
            t += cycle[i]
            if i+1 > K:
                break
            now = t
            if s > 0:
                e = (K-(i+1))//len(cycle)
                now += s * e
            ans = max(ans, now)
    print(ans)

=======
Suggestion 3

def main():
    # 读入数据
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # 从1开始编号，所以减1
    for i in range(N):
        P[i] -= 1

    # 一个周期的和
    cycle_sum = []
    # 一个周期的长度
    cycle_length = []

    # 一个周期的和
    for i in range(N):
        # 已经访问过的编号
        seen = []
        # 棋子的编号
        v = i
        # 一个周期的和
        cycle = 0
        # 一个周期的长度
        length = 0
        while True:
            seen.append(v)
            cycle += C[v]
            length += 1
            v = P[v]
            if v in seen:
                break
        cycle_sum.append(cycle)
        cycle_length.append(length)

    # 答案
    ans = -10 ** 18

    # 一个周期一个周期地考虑
    for i in range(N):
        # 一个周期的和
        s = 0
        # 一个周期的长度
        l = 0
        # 从i开始，最多走K步
        for j in range(min(K, cycle_length[i])):
            s += C[P[i]]
            i = P[i]
            l += 1
            ans = max(ans, s)
            # 如果可以继续走，那么就看看走下去的话，可以得到多少分
            if K - j - 1 > 0:
                # 剩下的步数
                r = K - j - 1
                # 剩下的步数里，可以走的周期数
                q = r // cycle_length[i]
                # 剩下的步数里，可以走的周期以外的步数
                w = r % cycle_length[i]
                # 周期的和
                t = cycle_sum[i] * q
                # 周期以外的和
                if w > 0:
                    t += max(cycle

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10**18
    for i in range(N):
        now = i
        score = 0
        cnt = 0
        while True:
            now = P[now] - 1
            score += C[now]
            cnt += 1
            if now == i:
                break
            if cnt == K:
                break
        if cnt < K:
            if score > 0:
                score += (K // cnt - 1) * score
            for j in range(K % cnt):
                now = P[now] - 1
                score += C[now]
        ans = max(ans, score)
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    p = [i - 1 for i in p]
    ans = -float('inf')
    for i in range(n):
        score = 0
        cnt = 0
        v = i
        while True:
            v = p[v]
            score += c[v]
            cnt += 1
            if cnt == k:
                break
            if score > ans:
                ans = score
            if v == i:
                break
    print(ans)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    c = list(map(int,input().split()))
    ans = -10**18
    for i in range(n):
        x = i
        s = 0
        l = 0
        while True:
            x = p[x] - 1
            s += c[x]
            l += 1
            if x == i:
                break
            if l == k:
                break
        t = 0
        for j in range(l):
            x = p[x] - 1
            t += c[x]
            ans = max(ans,t + (k - j - 1) // l * s)
    print(ans)

main()

=======
Suggestion 8

def main():
    N = int(input())
    K = int(input())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    #print(N, K, P, C)
    #print(len(P), len(C))
    max_sum = -10**9
    for i in range(N):
        #print(i)
        #print('P[i] = ', P[i])
        #print('C[i] = ', C[i])
        #print('max_sum = ', max_sum)
        #print('K = ', K)
        #print('P[P[i]-1] = ', P[P[i]-1])
        #print('C[P[i]-1] = ', C[P[i]-1])
        sum = 0
        j = i
        for _ in range(K):
            sum += C[P[j]-1]
            j = P[j]-1
            if sum > max_sum:
                max_sum = sum
            if j == i:
                break
    print(max_sum)

=======
Suggestion 9

def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10 ** 18
    for i in range(n):
        s = 0
        v = i
        for j in range(k):
            v = p[v] - 1
            s += c[v]
            ans = max(ans, s)
            if v == i:
                break
    print(ans)

solve()
