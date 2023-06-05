Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    a = [0] * M
    b = [0] * M
    for i in range(M):
        a[i], b[i] = map(int, input().split())
    print(N - 1 - M)

=======
Suggestion 2

def find(x):
    if par[x]==x:
        return x
    else:
        par[x]=find(par[x])
        return par[x]

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = [0]*m
    b = [0]*m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    print(m - len(set(a+b)))

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    ab = []
    for _ in range(m):
        a, b = map(int, input().split())
        ab.append((a, b))
    ab.sort(key=lambda x: x[1])
    ans = 0
    now = 0
    for a, b in ab:
        if a > now:
            now = b - 1
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = []
    for i in range(M):
        AB.append(list(map(int, input().split())))
    #print("N=", N)
    #print("M=", M)
    #print("AB=", AB)
    #print("AB[0][0]=", AB[0][0])
    #print("AB[0][1]=", AB[0][1])
    #print("AB[1][0]=", AB[1][0])
    #print("AB[1][1]=", AB[1][1])
    #print("AB[2][0]=", AB[2][0])
    #print("AB[2][1]=", AB[2][1])
    #print("AB[3][0]=", AB[3][0])
    #print("AB[3][1]=", AB[3][1])
    #print("AB[4][0]=", AB[4][0])
    #print("AB[4][1]=", AB[4][1])
    #print("AB[5][0]=", AB[5][0])
    #print("AB[5][1]=", AB[5][1])
    #print("AB[6][0]=", AB[6][0])
    #print("AB[6][1]=", AB[6][1])
    #print("AB[7][0]=", AB[7][0])
    #print("AB[7][1]=", AB[7][1])
    #print("AB[8][0]=", AB[8][0])
    #print("AB[8][1]=", AB[8][1])
    #print("AB[9][0]=", AB[9][0])
    #print("AB[9][1]=", AB[9][1])
    #print("AB[10][0]=", AB[10][0])
    #print("AB[10][1]=", AB[10][1])
    #print("AB[11][0]=", AB[11][0])
    #print("AB[11][1]=", AB[11][1])
    #print("AB[12][0]=", AB[12][0])
    #print("AB[12][1]=", AB[12][

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    bridges = []
    for i in range(M):
        a, b = map(int, input().split())
        bridges.append((a, b))
    bridges.sort()
    print(bridges)
    print(N, M)

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    a = []
    b = []
    for i in range(M):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    print(a,b)
    a.sort()
    b.sort()
    print(a,b)
    print(a[-1],b[0])
    if a[-1] <= b[0]:
        print(b[0]-a[-1])
    else:
        print(0)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    #print(a)
    #print(b)
    #print(n)
    #print(m)
    #print(len(a))
    #print(len(b))
    #print(a[0])
    #print(a[1])
    #print(b[0])
    #print(b[1])
    #print(a[0] == 1)
    #print(a[1] == 2)
    #print(b[0] == 4)
    #print(b[1] == 5)
    #print(a[0] == 1 and b[0] == 4)
    #print(a[1] == 2 and b[1] == 5)
    #print(a[0] == 1 and b[0] == 4 or a[1] == 2 and b[1] == 5)
    #print(a[0] == 1 and b[0] == 4 or a[1] == 2 and b[1] == 5 or a[2] == 3 and b[2] == 6)
    #print(a[0] == 1 and b[0] == 4 or a[1] == 2 and b[1] == 5 or a[2] == 3 and b[2] == 6 or a[3] == 4 and b[3] == 7)
    #print(a[0] == 1 and b[0] == 4 or a[1] == 2 and b[1] == 5 or a[2] == 3 and b[2] == 6 or a[3] == 4 and b[3] == 7 or a[4] == 5 and b[4] == 8)
    #print(a[0] == 1 and b[0] == 4 or a[1] == 2 and b[1] == 5 or a[2] == 3 and b[2] == 6 or a[3] == 4 and b[3] == 7 or

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    ab = []
    for i in range(M):
        a, b = map(int, input().split())
        ab.append((a, b))
    print(ab)
    print(N, M)
