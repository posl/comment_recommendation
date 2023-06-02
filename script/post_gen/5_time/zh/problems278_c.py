Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,q = map(int,input().split())
    #print(n,q)
    #print(type(n),type(q))
    #print(type(n))
    #

=======
Suggestion 2

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    follow = []
    for i in range(Q):
        follow.append(list(map(int, input().split())))

    follow.reverse()
    #print(follow)
    follow_list = []
    for i in range(Q):
        if follow[i][0] == 1:
            follow_list.append([follow[i][1], follow[i][2]])
        elif follow[i][0] == 2:
            follow_list.remove([follow[i][1], follow[i][2]])
        else:
            if [follow[i][1], follow[i][2]] in follow_list and [follow[i][2], follow[i][1]] in follow_list:
                print("Yes")
            else:
                print("No")

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    follow = [[0] * N for _ in range(N)]
    for _ in range(Q):
        t, a, b = map(int, input().split())
        a -= 1
        b -= 1
        if t == 1:
            follow[a][b] = 1
        elif t == 2:
            follow[a][b] = 0
        else:
            if follow[a][b] == 1:
                print("Yes")
            else:
                print("No")

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    follow = []
    for _ in range(Q):
        follow.append(list(map(int, input().split())))
    print(follow)
    for i in range(Q):
        if follow[i][0] == 3:
            if follow[i][1] == follow[i][2]:
                print("Yes")
            else:
                print("No")
        else:
            pass

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    follow = [[0 for i in range(N)] for j in range(N)]
    for i in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow[a-1][b-1] = 1
        elif t == 2:
            follow[a-1][b-1] = 0
        else:
            if follow[a-1][b-1] == 1 and follow[b-1][a-1] == 1:
                print("Yes")
            else:
                print("No")

=======
Suggestion 7

def is_followed_by(i, j):
    return i in follow[j]

=======
Suggestion 8

def problem278_c():
    pass

=======
Suggestion 9

def main():
    n,q = map(int,input().split())
    follow = set()
    for i in range(q):
        t,a,b = map(int,input().split())
        if t == 1:
            follow.add((a,b))
        elif t == 2:
            follow.discard((a,b))
        else:
            if (a,b) in follow and (b,a) in follow:
                print('Yes')
            else:
                print('No')

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    follow = []
    for i in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow.append([a, b])
        elif t == 2:
            follow.remove([a, b])
        else:
            if [a, b] in follow and [b, a] in follow:
                print('Yes')
            else:
                print('No')
