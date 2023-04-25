Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    D = sorted(range(N), key=lambda x: (A[x], B[x], C[x], x), reverse=True)
    E = D[:X] + D[X:X+Y] + D[X+Y:X+Y+Z]
    print(*sorted(E), sep='

')

=======
Suggestion 2

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append([A[i], B[i], A[i] + B[i], i + 1])
    C.sort(key=lambda x: x[0], reverse=True)
    D = []
    for i in range(X):
        D.append(C[i])
    C.sort(key=lambda x: x[1], reverse=True)
    for i in range(Y):
        D.append(C[i])
    C.sort(key=lambda x: x[2], reverse=True)
    for i in range(Z):
        D.append(C[i])
    D.sort(key=lambda x: x[3])
    for i in range(len(D)):
        print(D[i][3])

=======
Suggestion 3

def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append([a[i], b[i], a[i] + b[i], i + 1])
    c.sort(key=lambda x: (x[0], -x[1], -x[2], x[3]), reverse=True)
    for i in range(x + y + z):
        if i < x:
            print(c[i][3])
        elif i < x + y:
            if c[i][0] != c[i - 1][0]:
                print(c[i][3])
        else:
            if c[i][0] != c[i - 1][0] and c[i][1] != c[i - 1][1]:
                print(c[i][3])

=======
Suggestion 4

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [(A[i] + B[i], i + 1) for i in range(N)]
    C.sort(reverse=True)
    print(*[C[i][1] for i in range(X + Y + Z)], sep='

')

=======
Suggestion 5

def main():
    N,X,Y,Z = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = [A[i]+B[i] for i in range(N)]
    A = [(A[i],i+1) for i in range(N)]
    B = [(B[i],i+1) for i in range(N)]
    C = [(C[i],i+1) for i in range(N)]
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    D = []
    for i in range(X):
        D.append(A[i][1])
    for i in range(Y):
        D.append(B[i][1])
    for i in range(Z):
        D.append(C[i][1])
    D.sort()
    for i in range(X+Y+Z):
        print(D[i])

=======
Suggestion 6

def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x, y: x + y, a, b))
    d = sorted([(a[i], b[i], c[i], i + 1) for i in range(n)], reverse=True)
    e = d[:x]
    f = sorted(d[x:x + y], reverse=True)
    g = sorted(d[x + y:x + y + z], reverse=True)
    h = set([e[i][3] for i in range(len(e))])
    h |= set([f[i][3] for i in range(len(f))])
    h |= set([g[i][3] for i in range(len(g))])
    for i in sorted(h):
        print(i)

=======
Suggestion 7

def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = [(a[i], b[i], a[i] + b[i], i + 1) for i in range(n)]
    c.sort(key=lambda x: (-x[0], x[3]))
    c.sort(key=lambda x: (-x[2], x[3]))
    c.sort(key=lambda x: (-x[1], x[3]))

    for i in range(x):
        print(c[i][3])
    for i in range(y):
        print(c[i + x][3])
    for i in range(z):
        print(c[i + x + y][3])

=======
Suggestion 8

def main():
    #n: number of examinees
    #x: number of examinees with the highest math scores admitted
    #y: number of examinees with the highest English scores admitted
    #z: number of examinees with the highest total scores admitted
    #a: math scores
    #b: English scores
    #t: total scores
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    t = [a[i]+b[i] for i in range(n)]

    #sort by math score
    d = sorted([(a[i],b[i],t[i],i+1) for i in range(n)],reverse=True)

    #admit x examinees with the highest math scores
    for i in range(x):
        print(d[i][3])

    #sort by English score
    d = sorted([(a[i],b[i],t[i],i+1) for i in range(n) if i not in range(x)],reverse=True)

    #admit y examinees with the highest English scores
    for i in range(y):
        print(d[i][3])

    #sort by total score
    d = sorted([(a[i],b[i],t[i],i+1) for i in range(n) if i not in range(x+y)],reverse=True)

    #admit z examinees with the highest total scores
    for i in range(z):
        print(d[i][3])

=======
Suggestion 9

def main():
  # Read the input
  N, X, Y, Z = map(int, input().split())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))

  # Prepare the list of the examinees
  examinees = []
  for i in range(N):
    examinees.append((A[i], B[i], A[i]+B[i], i+1))

  # Sort the list of the examinees in the descending order by the total score
  examinees.sort(key=lambda x: x[2], reverse=True)

  # Admit the examinees with the highest total scores
  admitted = examinees[:Z]

  # Sort the list of the examinees in the descending order by the English score
  examinees.sort(key=lambda x: x[1], reverse=True)

  # Admit the examinees with the highest English scores
  admitted += examinees[:Y]

  # Sort the list of the examinees in the descending order by the math score
  examinees.sort(key=lambda x: x[0], reverse=True)

  # Admit the examinees with the highest math scores
  admitted += examinees[:X]

  # Sort the list of the examinees in the ascending order by the examinee number
  admitted.sort(key=lambda x: x[3])

  # Print the examinee numbers of the admitted examinees
  for examinee in admitted:
    print(examinee[3])

main()

I am sending you the codedump of Python3: How to sort a list of tuples in descending order by the first element, then by the second element, and so on? that you can see here: https://codedump.io/share/7s0nTlTn7VrG/1

=======
Suggestion 10

def read_ints():
    return map(int, raw_input().split())
