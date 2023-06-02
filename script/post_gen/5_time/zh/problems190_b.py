Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n, s, d = map(int, input().split())
    spells = []
    for i in range(n):
        spells.append(list(map(int, input().split())))
    return n, s, d, spells

=======
Suggestion 2

def solve():
    N, S, D = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(N)]
    for x, y in XY:
        if x < S and y > D:
            print('Yes')
            return
    print('No')

=======
Suggestion 3

def main():
    n,s,d = input().split()
    n,s,d = int(n),int(s),int(d)
    lst = []
    for i in range(n):
        x,y = input().split()
        x,y = int(x),int(y)
        lst.append([x,y])
    for item in lst:
        if item[0] < s and item[1] > d:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 4

def judge(n,s,d,x,y):
    for i in range(n):
        if x[i] < s and y[i] > d:
            return True
    return False

n,s,d = map(int,input().split())
x = []
y = []
for i in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)

=======
Suggestion 5

def main():
    n, s, d = map(int, input().split())
    for i in range(n):
        x, y = map(int, input().split())
        if x < s and y > d:
            print("Yes")
            return
    print("No")

main()

=======
Suggestion 6

def solve():
    n, s, d = map(int, input().split())
    for i in range(n):
        x, y = map(int, input().split())
        if x < s and y > d:
            print('Yes')
            return
    print('No')
solve()

=======
Suggestion 7

def main():
    n,s,d = map(int, input().split())
    flag = False
    for i in range(n):
        x,y = map(int, input().split())
        if x < s and y > d:
            flag = True
    if flag:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    n, s, d = map(int, input().split())
    for i in range(n):
        x, y = map(int, input().split())
        if x < s and y > d:
            print("Yes")
            return
    print("No")

=======
Suggestion 9

def main():
    n,s,d = map(int,input().split())
    for i in range(n):
        x,y = map(int,input().split())
        if x < s and y > d:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 10

def solve():
    N,S,D = map(int,input().split())
    for i in range(N):
        X,Y = map(int,input().split())
        if X < S and Y > D:
            print('Yes')
            return
    print('No')
solve()
