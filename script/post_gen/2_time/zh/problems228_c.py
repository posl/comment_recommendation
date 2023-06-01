Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a[x-1] = 0
    count = 1
    for i in range(n):
        if a[i] != 0:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i-1 for i in a]
    b = [0]*n
    b[x-1] = 1
    for i in range(n):
        if b[i] == 1:
            b[a[i]] = 1
    print(sum(b))

=======
Suggestion 3

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))

    a[x-1] = 0
    ans = 1
    for i in range(n):
        if a[i] != 0:
            ans += 1
    print(ans)

main()

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = [False] * n
    b[x - 1] = True
    for i in range(n):
        if b[i]:
            a[i] -= 1
            b[a[i]] = True
    print(b.count(True))

=======
Suggestion 5

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a[x-1] = 0
    b = [0]*n
    for i in range(n):
        if a[i] != 0:
            b[a[i]-1] += 1
    print(b.count(max(b)))

=======
Suggestion 6

def get_input():
    n_x = input().split()
    n = int(n_x[0])
    x = int(n_x[1])
    a = input().split()
    a = [int(i) for i in a]
    return n, x, a

=======
Suggestion 7

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.insert(0,0)
    b = [0 for i in range(n+1)]
    b[x] = 1
    cnt = 1
    for i in range(1,n+1):
        if b[a[i]] == 0:
            b[a[i]] = 1
            cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a[x-1] = 0
    for i in range(n):
        if a[i] != 0:
            a[a[i]-1] = 0
    print(n - a.count(0))

=======
Suggestion 9

def check_friend(friends, friend_id, secret_owner):
    if friend_id == secret_owner:
        return True
    elif friends[friend_id] == secret_owner:
        return True
    else:
        return check_friend(friends, friends[friend_id], secret_owner)

=======
Suggestion 10

def f(n,x,l):
    d = {}
    for i in range(n):
        d[i+1] = 0
    d[x] = 1
    for i in range(n):
        if d[l[i]] == 1:
            d[i+1] = 1
    return sum(d.values())
