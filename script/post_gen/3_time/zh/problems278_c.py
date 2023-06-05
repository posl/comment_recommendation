Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
	n, q = map(int, input().split())
	# print(n, q)

=======
Suggestion 2

def main():
    n,q = map(int,input().split())
    #print(n,q)
    #print(type(n))

=======
Suggestion 3

def find(a):
    if a == root[a]:
        return a
    else:
        root[a] = find(root[a])
        return root[a]

=======
Suggestion 4

def main():
    n,q = map(int,input().split())
    follow = []
    for i in range(n):
        follow.append([0]*n)
    for i in range(q):
        t,a,b = map(int,input().split())
        if t == 1:
            follow[a-1][b-1] = 1
        elif t == 2:
            follow[a-1][b-1] = 0
        else:
            if follow[a-1][b-1] == 1 and follow[b-1][a-1] == 1:
                print('Yes')
            else:
                print('No')

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    follow = set()
    follow_back = set()
    for i in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow.add((a, b))
        elif t == 2:
            follow_back.add((a, b))
        else:
            if (a, b) in follow and (b, a) in follow_back:
                print('Yes')
            else:
                print('No')

=======
Suggestion 6

def follow(a, b):
    if a in following[b] and b in following[a]:
        return True
    else:
        return False

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    follow = {}
    followed = {}
    for i in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            follow.setdefault(a, set()).add(b)
            followed.setdefault(b, set()).add(a)
        elif t == 2:
            follow.setdefault(a, set()).discard(b)
            followed.setdefault(b, set()).discard(a)
        elif t == 3:
            if follow.get(a, set()) & followed.get(b, set()):
                print("Yes")
            else:
                print("No")

=======
Suggestion 9

def main():
    n, q = map(int, input().split())
    follow = []
    for i in range(q):
        follow.append(list(map(int, input().split())))
    for i in range(q):
        if follow[i][0] == 3:
            if follow[i][1] == follow[i][2]:
                print("Yes")
                continue
            if [follow[i][2], follow[i][1]] in follow:
                print("Yes")
            else:
                print("No")

=======
Suggestion 10

def main():
    n,q = map(int,input().split())
    follow = [set() for _ in range(n)]
    for _ in range(q):
        t,a,b = map(int,input().split())
        a -= 1
        b -= 1
        if t == 1:
            follow[a].add(b)
        elif t == 2:
            follow[a].discard(b)
        elif t == 3:
            print("Yes" if b in follow[a] else "No")
