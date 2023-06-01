Synthesizing 10/10 solutions

=======
Suggestion 1

def get_depth(p, depth):
    if p == 1:
        return depth
    else:
        return get_depth(parents[p], depth+1)

N = int(input())
parents = list(map(int, input().split()))
depth = 0
for i in range(N):
    depth = max(depth, get_depth(i+1, 1))
print(depth)

=======
Suggestion 2

def dfs(start, depth, max_depth, parents):
    if depth > max_depth:
        max_depth = depth
    if start in parents:
        max_depth = dfs(parents[start], depth+1, max_depth, parents)
    return max_depth

=======
Suggestion 3

def getGeneration(n, p):
    maxGeneration = 0
    for i in range(1, n + 1):
        generation = 1
        parent = p[i - 1]
        while parent != -1:
            generation += 1
            parent = p[parent - 1]
        if generation > maxGeneration:
            maxGeneration = generation
    return maxGeneration

=======
Suggestion 4

def generation(n, p):
    if n == 1:
        return 0
    else:
        return generation(p[n-2], p) + 1

=======
Suggestion 5

def main():
    # 读取输入
    N = int(input())
    P = list(map(int, input().split()))

    # 从第i个人开始，向上追溯到第1个人，计算代数
    ans = 0
    for i in range(N):
        p = i + 1
        while p != -1:
            ans += 1
            p = P[p - 1]
            # print(p)
        # print('---')
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        cnt = 0
        j = i
        while j != -1:
            j = p[j] - 1
            cnt += 1
        ans = max(ans, cnt)
    print(ans)

=======
Suggestion 7

def func():
    n=int(input())
    p=list(map(int,input().split()))
    p.insert(0,0)
    ans=0
    for i in range(1,n+1):
        cnt=0
        j=i
        while j!=1:
            j=p[j]
            cnt+=1
        ans=max(ans,cnt)
    print(ans+1)
func()

=======
Suggestion 8

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N - 1):
        count = 0
        j = i
        while True:
            if P[j] - 1 == i:
                break
            count += 1
            j = P[j] - 1
        if count > ans:
            ans = count
    print(ans + 1)

=======
Suggestion 9

def problem263_b():
    n = int(input())
    p = [0] + list(map(int, input().split()))
    d = [0] * (n + 1)
    for i in range(n, 0, -1):
        d[i] = d[p[i]] + 1
    print(max(d))

=======
Suggestion 10

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p.insert(0, 0)
    max = 0
    for i in range(1, n+1):
        count = 0
        j = i
        while p[j] != -1:
            j = p[j]
            count += 1
        if count > max:
            max = count
    print(max+1)
