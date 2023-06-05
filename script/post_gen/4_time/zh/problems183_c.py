Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_city_list(city_num):
    if city_num == 1:
        return [1]
    city_list = []
    for i in range(1, city_num+1):
        city_list.append(i)
    return city_list

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    T = []
    for i in range(N):
        T.append(list(map(int, input().split())))
    # print(T)
    # print(len(T))

    # 递归函数
    def dfs(i, j, t, visited):
        visited = visited[:]
        visited.append(j)
        if len(visited) == N:
            if t + T[i][j] == K:
                return 1
            else:
                return 0
        else:
            ans = 0
            for k in range(N):
                if k not in visited:
                    ans += dfs(j, k, t + T[i][j], visited)
            return ans

    ans = 0
    for i in range(N):
        ans += dfs(i, i, 0, [])
    print(ans)

=======
Suggestion 4

def dfs(path, n, k, t, visited, cur, ans):
    if len(path) == n:
        if k == t[path[-1]][0]:
            ans[0] += 1
        return
    for i in range(1, n):
        if visited[i] == 0:
            visited[i] = 1
            path.append(i)
            dfs(path, n, k, t, visited, i, ans)
            path.pop()
            visited[i] = 0

=======
Suggestion 5

def dfs(x, y, t):
    global ans
    if x == n - 1:
        if t + a[y][0] == k:
            ans += 1
    else:
        for i in range(1, n):
            if not used[i]:
                used[i] = True
                dfs(x + 1, i, t + a[y][i])
                used[i] = False


n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
used = [False] * n
used[0] = True
ans = 0
dfs(0, 0, 0)
print(ans)

=======
Suggestion 6

def get_time(n, k):
    times = []
    for i in range(n):
        times.append(list(map(int, input().split())))
    # print(times)
    return times

=======
Suggestion 7

def dfs(now, visited, cost):
    global ans, N, K, T
    visited = visited | (1 << now)
    if visited == (1 << N) - 1 and cost + T[now][0] == K:
        ans += 1
    else:
        for i in range(N):
            if not visited & (1 << i):
                dfs(i, visited, cost + T[now][i])

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(0, 0, 0)
print(ans)

=======
Suggestion 8

def main():
    # 获取输入
    n, k = map(int, input().split())
    t = []
    for i in range(n):
        t.append(list(map(int, input().split())))
    # 从1号城市开始，访问其他城市的所有路径
    city = [i for i in range(1, n)]
    # 计算路径总时间
    total_time = 0
    for i in range(n - 1):
        total_time += t[city[i - 1]][city[i]]
    # 计算路径总数
    total_count = 0
    while True:
        # 递增最后一个访问的城市
        city[-1] += 1
        # 最后一个访问城市超出范围，回溯
        if city[-1] >= n:
            # 没有访问城市，退出
            if len(city) == 1:
                break
            # 最后一个访问城市回到1号城市，删除最后一个访问城市，继续回溯
            elif city[-1] == 1:
                city.pop()
            # 最后一个访问城市不是1号城市，继续回溯
            else:
                continue
        # 计算路径总时间
        total_time = 0
        for i in range(n - 1):
            total_time += t[city[i - 1]][city[i]]
        # 路径总时间等于k，路径总数加1
        if total_time == k:
            total_count += 1
    # 打印答案
    print(total_count)
