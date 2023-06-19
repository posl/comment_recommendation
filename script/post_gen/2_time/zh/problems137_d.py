Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    import heapq
    heap = []
    ans = 0
    j = 0
    for i in range(1, M + 1):
        while j < N and AB[j][0] == i:
            heapq.heappush(heap, -AB[j][1])
            j += 1
        if heap:
            ans += -heapq.heappop(heap)
    print(ans)

=======
Suggestion 2

def solve():
    N, M = map(int, input().split())
    works = []
    for i in range(N):
        works.append(list(map(int, input().split())))
    works.sort(key=lambda x: x[0])
    ans = 0
    i = 0
    while M > 0:
        if works[i][0] > M:
            break
        else:
            ans += works[i][1]
            M -= works[i][0]
            i += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    jobs = [list(map(int, input().split())) for i in range(N)]
    jobs.sort(key=lambda x:x[0])
    ans = 0
    i = 0
    while i < N:
        if M >= jobs[i][0]:
            ans += jobs[i][1]
            M -= 1
        else:
            break
        i += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    works = []
    for i in range(N):
        works.append(tuple(map(int, input().split())))
    works.sort(key=lambda x:x[0])
    ans = 0
    day = 0
    for i in range(N):
        if day + works[i][0] <= M:
            ans += works[i][1]
            day += works[i][0]
    print(ans)

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def getMaxReward(N,M,work):
    work.sort(key=lambda x:x[0])
    work.sort(key=lambda x:x[1],reverse=True)
    #print(work)
    reward = [0 for i in range(M)]
    for i in range(N):
        for j in range(work[i][0]-1,M):
            if reward[j] == 0:
                reward[j] = work[i][1]
                break
    return sum(reward)

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int,input().split())))
    AB.sort(key=lambda x:x[0])
    AB.sort(key=lambda x:x[1],reverse=True)
    ans = 0
    for i in range(M):
        ans += AB[i][1]
    print(ans)

=======
Suggestion 8

def main():
    # 读入数据
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    # 按照a_i的升序排序
    ab.sort(key=lambda x: x[0])
    # 用于记录已经完成的工作
    done = []
    # 用于记录已经完成的工作的奖励
    done_b = []
    # 用于记录已经完成的工作的奖励的累计
    done_b_sum = []
    # 用于记录已经完成的工作的奖励的累计的最大值
    done_b_sum_max = []
    # 用于记录已经完成的工作的奖励的累计的最大值的累计
    done_b_sum_max_sum = []
    # 用于记录已经完成的工作的奖励的累计的最大值的累计的最大值
    done_b_sum_max_sum_max = []
    # 用于记录已经完成的工作的奖励的累计的最大值的累计的最大值的累计
    done_b_sum_max_sum_max_sum = []
    # 用于记录已经完成的工作的奖励的累计的最大值的累计的最大值的累计的最大值
    done_b_sum_max_sum_max_sum_max = []
    # 用于记录已经完成的工作的奖励的累计的最大值的累计的最大值的累计的最大值的累计
    done_b_sum_max_sum_max_sum_max_sum = []
    # 用于记录已经完成的工作的奖励的累计的最大值的累计的最大值的累计的最大值的累计的最大值
    done_b_sum_max_sum_max_sum_max_sum_max = []
    # 用于记录已经完成的工作的奖励的累计的最大值的累计的最

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    ab = []
    for i in range(n):
        ab.append(list(map(int,input().split())))
    ab.sort(key=lambda x:x[0])
    ab.sort(key=lambda x:x[1],reverse=True)
    print(ab)
    ans = 0
    for i in range(n):
        if m >= ab[i][0]:
            ans += ab[i][1]
            m -= ab[i][0]
        else:
            ans += m * ab[i][1]
            break
    print(ans)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort()
    from collections import deque
    dq = deque()
    ans = 0
    i = 0
    for day in range(1, m + 1):
        while i < n and jobs[i][0] <= day:
            dq.append(jobs[i][1])
            i += 1
        if dq:
            ans += dq.pop()
    print(ans)
