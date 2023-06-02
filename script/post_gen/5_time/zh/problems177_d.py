Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    friends = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        friends[a - 1].append(b - 1)
        friends[b - 1].append(a - 1)
    # print(friends)
    group = [0] * N
    group_num = 0
    for i in range(N):
        if group[i] == 0:
            group_num += 1
            group[i] = group_num
            stack = [i]
            while stack:
                j = stack.pop()
                for k in friends[j]:
                    if group[k] == 0:
                        group[k] = group_num
                        stack.append(k)
    print(group_num)

=======
Suggestion 3

def solve():
    pass

=======
Suggestion 4

def find(x):
    if x!=p[x]:
        p[x]=find(p[x])
    return p[x]

=======
Suggestion 5

def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A, B = [], []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(A)
    print(B)

=======
Suggestion 7

def find(a, x):
    if a[x] == x:
        return x
    else:
        a[x] = find(a, a[x])
        return a[x]

=======
Suggestion 8

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
