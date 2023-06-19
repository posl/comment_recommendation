Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    l.sort()
    sum = 0
    for i in range(n):
        if m >= l[i][1]:
            sum += l[i][0] * l[i][1]
            m -= l[i][1]
        else:
            sum += l[i][0] * m
            break
    print(sum)

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort()
    ans = 0
    for a,b in ab:
        ans += a*b
        m -= b
        if m <= 0:
            ans -= m*a
            break
    print(ans)

=======
Suggestion 3

def main():
    N,M=map(int,input().split())
    AB=[list(map(int,input().split())) for _ in range(N)]
    AB.sort()
    ans=0
    for i in range(N):
        if M>AB[i][1]:
            ans+=AB[i][0]*AB[i][1]
            M-=AB[i][1]
        else:
            ans+=AB[i][0]*M
            break
    print(ans)
main()

=======
Suggestion 4

def readinput():
    n,m = map(int,input().split())
    ab=[]
    for _ in range(n):
        a,b = map(int,input().split())
        ab.append([a,b])
    return n,m,ab

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort(key=lambda x: x[0])

    ans = 0
    for i in range(n):
        if m <= 0:
            break
        a, b = arr[i]
        if m >= b:
            ans += a * b
            m -= b
        else:
            ans += a * m
            m = 0
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    shops = []
    for i in range(n):
        a, b = map(int, input().split())
        shops.append((a, b))
    shops.sort(key=lambda x: x[0])
    count = 0
    money = 0
    for i in range(n):
        if count + shops[i][1] < m:
            money += shops[i][0] * shops[i][1]
            count += shops[i][1]
        else:
            money += shops[i][0] * (m - count)
            count = m
            break
    print(money)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    # print(N, M)
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # print(A, B)
    # print('------')
    # print(sorted(B))
    # print('------')
    # print(sorted(B, reverse=True))
    # print('------')
    # print(sorted(zip(B, A)))
    # print('------')
    # print(sorted(zip(B, A), reverse=True))
    # print('------')
    # print(sorted(zip(B, A), reverse=True)[:M])
    # print('------')
    # print(sorted(zip(B, A), reverse=True)[:M][0])
    # print('------')
    # print(sorted(zip(B, A), reverse=True)[:M][0][0])
    # print('------')
    # print(sorted(zip(B, A), reverse=True)[:M][0][1])
    # print('------')
    # print(sorted(zip(B, A), reverse=True)[:M][0][0] * sorted(zip(B, A), reverse=True)[:M][0][1])
    # print('------')
    # print(sum([sorted(zip(B, A), reverse=True)[:M][i][0] * sorted(zip(B, A), reverse=True)[:M][i][1] for i in range(M)]))
    # print('------')
    print(sum([sorted(zip(B, A), reverse=True)[:M][i][0] * sorted(zip(B, A), reverse=True)[:M][i][1] for i in range(M)]))

=======
Suggestion 8

def main():
    n,m = [int(x) for x in input().split()]
    a = []
    b = []
    for i in range(n):
        a1,b1 = [int(x) for x in input().split()]
        a.append(a1)
        b.append(b1)
    # print(a)
    # print(b)
    # print(n,m)
    c = list(zip(a,b))
    # print(c)
    c.sort(key=lambda x:x[0])
    # print(c)
    sum = 0
    i = 0
    while m > 0:
        if m >= c[i][1]:
            sum += c[i][0] * c[i][1]
            m -= c[i][1]
        else:
            sum += c[i][0] * m
            m -= m
        i += 1
    print(sum)

=======
Suggestion 9

def get_input():
    n,m = map(int, input().split())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    return n,m,ab

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    #print(n, m)
    #print(type(n))
    #print(type(m))
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    #print(a)
    #print(b)
    #print(type(a))
    #print(type(b))
    #print(sum(b))
    if sum(b) <= m:
        print(sum([a[i] * b[i] for i in range(n)]))
    else:
        b_a = list(zip(a, b))
        b_a.sort()
        #print(b_a)
        #print(type(b_a))
        #print(b_a[0][0])
        #print(b_a[0][1])
        #print(b_a[1][0])
        #print(b_a[1][1])
        #print(b_a[2][0])
        #print(b_a[2][1])
        #print(b_a[3][0])
        #print(b_a[3][1])
        #print(b_a[4][0])
        #print(b_a[4][1])
        #print(b_a[5][0])
        #print(b_a[5][1])
        #print(b_a[6][0])
        #print(b_a[6][1])
        #print(b_a[7][0])
        #print(b_a[7][1])
        #print(b_a[8][0])
        #print(b_a[8][1])
        #print(b_a[9][0])
        #print(b_a[9][1])
        #print(b_a[10][0])
        #print(b_a[10][1])
        #print(b_a[11][0])
        #print(b_a[11][1])
        #print(b_a[12][0])
        #print(b_a[12][1])
        #print(b_a[13][0])
        #print(b_a[13][1])
        #print(b_a[14][0])
        #print(b_a[14][1])
        #print(b_a[15][0])
        #print(b_a[15][1])
        #print(b_a[16][0])
        #print(b_a[16][1])
