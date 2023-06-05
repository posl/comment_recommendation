Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(n, k, a):
    k = k % n
    for i in range(k):
        a = a[a[i] - 1]
    return a

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0 for i in range(n)]
    b[0] = 1
    now = 1
    for i in range(1,k+1):
        now = a[now-1]
        if b[now-1] == 0:
            b[now-1] = i+1
        else:
            loop = i+1-b[now-1]
            now = 1
            for j in range(k%loop):
                now = a[now-1]
            break
    print(now)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    k = k % n
    for i in range(k):
        a[i] = a[i] - 1
    for i in range(n):
        if i == 0:
            b = [a[i]]
        else:
            b.append(a[b[i-1]])
        if b[i] == 0:
            print(i+1)
            return
    print(b[k] + 1)

=======
Suggestion 4

def main():
    # 读入数据
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # 记录访问过的城市
    visited = [0] * n
    # 记录访问过的城市的顺序
    visited_order = []
    # 访问的城市
    city = 0
    # 访问的城市的顺序
    order = 1
    # 访问城市
    visited[city] = order
    visited_order.append(city)
    # 访问次数
    count = 1
    # 访问下一个城市
    city = a[city] - 1
    while True:
        # 如果访问过
        if visited[city] != 0:
            # 记录访问次数
            count = count - visited[city] + 1
            # 记录访问的城市的顺序
            visited_order = visited_order[visited[city] - 1:]
            break
        # 记录访问的城市
        visited[city] = order + 1
        visited_order.append(city)
        # 访问次数加一
        count += 1
        # 访问下一个城市
        city = a[city] - 1
        # 增加访问的城市的顺序
        order += 1
    # 访问次数取模
    k = k % count
    # 访问的城市的顺序
    visited_order = visited_order[:k]
    # 访问的城市
    city = visited_order[-1]
    # 访问次数
    count = len(visited_order)
    # 访问下一个城市
    city = a[city] - 1
    while True:
        # 访问次数加一
        count += 1
        # 访问下一个城市
        city = a[city] - 1
        # 如果访问过
        if city in visited_order:
            # 访问的城市的顺序
            visited

=======
Suggestion 5

def test():
    pass

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    town = 1
    for i in range(K):
        town = A[town-1]
    print(town)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    pos = 0
    pos_list = [0]
    for i in range(K):
        pos = A[pos] - 1
        if pos in pos_list:
            break
        else:
            pos_list.append(pos)
    if i == K - 1:
        print(pos + 1)
    else:
        print(pos_list[(K - 1) % (i + 1) + 1] + 1)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0,0)
    now = 1
    for i in range(K):
        now = A[now]
    print(now)

=======
Suggestion 9

def main():
    pass
