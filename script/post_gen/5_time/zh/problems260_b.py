Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append((a[i]+b[i],i+1))
    c.sort(key=lambda x:(x[0],x[1]),reverse=True)
    for i in range(x):
        print(c[i][1])
    for i in range(x,x+y):
        print(c[i][1])
    for i in range(x+y,x+y+z):
        print(c[i][1])

=======
Suggestion 2

def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [(i, a[i], b[i], a[i] + b[i]) for i in range(n)]
    c.sort(key=lambda x: -x[3])
    c.sort(key=lambda x: -x[2])
    c.sort(key=lambda x: -x[1])
    c = c[:x + y + z]
    c.sort()
    for i in c:
        print(i[0] + 1)

=======
Suggestion 3

def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append([i+1,a[i],b[i],a[i]+b[i]])
    c.sort(key=lambda x:(-x[1],-x[2],-x[3],x[0]))
    c = c[:x+y+z]
    c.sort(key=lambda x:x[0])
    for i in c:
        print(i[0])

=======
Suggestion 4

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    scores = []
    for i in range(N):
        scores.append((A[i], B[i], i + 1))

    scores.sort(reverse=True)
    scores = scores[:X + Y + Z]

    scores.sort(key=lambda x: x[1], reverse=True)
    scores = scores[:Y + Z]

    scores.sort(key=lambda x: x[0] + x[1], reverse=True)
    scores = scores[:Z]

    scores.sort(key=lambda x: x[2])

    for score in scores:
        print(score[2])

=======
Suggestion 5

def get_input():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    return n,x,y,z,a,b

=======
Suggestion 6

def get_score():
    n,x,y,z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append([a[i]+b[i],a[i],i+1])
    c.sort(reverse=True)
    c1 = c[:x]
    c2 = c[x:x+y]
    c3 = c[x+y:x+y+z]
    c1.sort(key=lambda x:x[2])
    c2.sort(key=lambda x:x[2])
    c3.sort(key=lambda x:x[2])
    for i in range(len(c1)):
        print(c1[i][2])
    for i in range(len(c2)):
        print(c2[i][2])
    for i in range(len(c3)):
        print(c3[i][2])

=======
Suggestion 7

def get_input():
    input_list = []
    while True:
        try:
            input_list.append(int(input()))
        except EOFError:
            break
    return input_list

=======
Suggestion 8

def get_input():
    line1 = input().split()
    line2 = input().split()
    line3 = input().split()
    return line1, line2, line3

=======
Suggestion 9

def main():
    N,X,Y,Z = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    score = []
    for i in range(N):
        score.append([A[i]+B[i],A[i],B[i],i+1])
    score.sort(reverse=True)
    for i in range(X):
        print(score[i][3])
    for i in range(X,X+Y):
        print(score[i][3])
    for i in range(X+Y,X+Y+Z):
        print(score[i][3])
