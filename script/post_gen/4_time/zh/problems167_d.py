Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    i = 0
    while k > 0:
        if i == n:
            i = 0
        k -= 1
        i = a[i] - 1
    print(i + 1)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    visited = [False for _ in range(N)]

    cnt = 0
    while not visited[0]:
        visited[cnt] = True
        cnt = A[cnt] - 1

    cnt2 = 0
    while visited[cnt]:
        visited[cnt] = False
        cnt = A[cnt] - 1
        cnt2 += 1

    K %= cnt2

    for _ in range(K):
        cnt = A[cnt] - 1

    print(cnt+1)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    next_town = [1]
    next_town.append(a[0])
    for i in range(n):
        next_town.append(a[next_town[-1]-1])
    #print(next_town)
    next_town = next_town[1:]
    #print(next_town)
    #print(next_town.index(next_town[-1]))
    #print(next_town[next_town.index(next_town[-1])+1:])
    if k <= next_town.index(next_town[-1]):
        print(next_town[k])
    else:
        k = k - next_town.index(next_town[-1])
        k = k % len(next_town[next_town.index(next_town[-1])+1:])
        print(next_town[next_town.index(next_town[-1])+1:][k])

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [1]
    for i in range(1, n+1):
        b.append(a[b[i-1]-1])
    c = [1]
    for i in range(1, n+1):
        c.append(b[i])
        if c.count(c[i]) == 2:
            break
    if k < i:
        print(c[k+1])
    else:
        print(c[(k-i)%(i+1)+i+1])

=======
Suggestion 5

def solve(n,k,a):
    a = [i-1 for i in a]
    s = [1]
    c = [0]*n
    c[0] = 1
    while c[s[-1]] == 0:
        s.append(a[s[-1]])
        c[s[-1]] = c[s[-2]]+1
    l = c[s[-1]]-1
    r = len(s)-1
    if k < l:
        print(s[k]+1)
    else:
        print(s[(k-l)%(r-l)+l]+1)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # print(N, K)
    # print(A)

    # 1. 以A[0]为起点，寻找环
    # 2. 求出环的长度
    # 3. 求出环的起点
    # 4. 求出环的终点
    # 5. 求出环的长度
    # 6. 求出环上第K个位置的元素

    # 1. 以A[0]为起点，寻找环
    # 2. 求出环的长度
    # 3. 求出环的起点
    # 4. 求出环的终点
    # 5. 求出环的长度
    # 6. 求出环上第K个位置的元素

    # 1. 以A[0]为起点，寻找环
    # 2. 求出环的长度
    # 3. 求出环的起点
    # 4. 求出环的终点
    # 5. 求出环的长度
    # 6. 求出环上第K个位置的元素

    # 1. 以A[0]为起点，寻找环
    # 2. 求出环的长度
    # 3. 求出环的起点
    # 4. 求出环的终点
    # 5. 求出环的长度
    # 6. 求出环上第K个位置的元素

    # 1. 以A[0]为起点，寻找环
    # 2. 求出环的长度
    # 3. 求出环的起点
    # 4. 求出环的终点
    # 5. 求出环的长度
    # 6. 求出环上第

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    t = [0] * N
    now = 0
    cnt = 0
    while t[now] == 0:
        t[now] = cnt
        cnt += 1
        now = A[now] - 1
    loop = cnt - t[now]
    if K < t[now]:
        now = 0
        for i in range(K):
            now = A[now] - 1
    else:
        K -= t[now]
        K %= loop
        now = 0
        for i in range(K):
            now = A[now] - 1
    print(now + 1)

=======
Suggestion 8

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    k -= 1
    visited = [False] * n
    visited[0] = True
    path = [0]
    while k:
        k -= 1
        path.append(a[path[-1]] - 1)
        if visited[path[-1]]:
            break
        visited[path[-1]] = True
    if k:
        print(path[k % len(path)] + 1)
    else:
        print(path[-1] + 1)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    i = 1
    for j in range(k):
        i = a[i-1]
    print(i)
