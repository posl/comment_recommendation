Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    L = []
    for _ in range(N):
        L.append(list(map(int, input().split())))

    L.sort()
    n = 1
    for i in range(1, N):
        if L[i] != L[i-1]:
            n += 1
    print(n)

=======
Suggestion 2

def main():
    n = int(input())
    #print(n)
    l = []
    for i in range(n):
        #print(i)
        l.append(list(map(int,input().split())))
    #print(l)
    l.sort()
    #print(l)

    ans = 1
    for i in range(n-1):
        if l[i] != l[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    d = {}
    for i in range(n):
        l = list(map(int, input().split()))
        l.pop(0)
        l = tuple(l)
        if l in d:
            d[l] += 1
        else:
            d[l] = 1
    print(len(d))

=======
Suggestion 4

def main():
    N = int(input())
    l_list = []
    for i in range(N):
        l_list.append(list(map(int, input().split())))
    l_list.sort()
    count = 1
    for i in range(N-1):
        if l_list[i] != l_list[i+1]:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append([int(i) for i in input().split()])
    l.sort(key=lambda x: x[1:])
    count = 1
    for i in range(n-1):
        if l[i] != l[i+1]:
            count += 1
    print(count)

=======
Suggestion 6

def problems226_b():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    a.sort()
    ans = 0
    for i in range(n):
        if i == 0:
            ans += 1
        else:
            for j in range(i):
                if a[i] == a[j]:
                    break
                if j == i - 1:
                    ans += 1
    print(ans)

=======
Suggestion 7

def func_226_b(n, l, a):
    #a = [list(map(int, input().split())) for _ in range(n)]
    #print(a)
    #print(a[0][0])
    #print(a[0][1])
    #print(a[0][2])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[1][2])
    #print(a[2][0])
    #print(a[2][1])
    #print(a[2][2])
    #print(a[3][0])
    #print(a[3][1])
    #print(a[3][2])
    #print(a[4][0])
    #print(a[4][1])
    #print(a[4][2])
    #print(a[5][0])
    #print(a[5][1])
    #print(a[5][2])
    #print(a[6][0])
    #print(a[6][1])
    #print(a[6][2])
    #print(a[7][0])
    #print(a[7][1])
    #print(a[7][2])
    #print(a[8][0])
    #print(a[8][1])
    #print(a[8][2])
    #print(a[9][0])
    #print(a[9][1])
    #print(a[9][2])
    #print(a[10][0])
    #print(a[10][1])
    #print(a[10][2])
    #print(a[11][0])
    #print(a[11][1])
    #print(a[11][2])
    #print(a[12][0])
    #print(a[12][1])
    #print(a[12][2])
    #print(a[13][0])
    #print(a[13][1])
    #print(a[13][2])
    #print(a[14][0])
    #print(a[14][1])
    #print(a[14][2])
    #print(a[15][0])
    #print(a[15][1])
    #print(a[15][2])
    #print(a[16][0])
    #print(a[16][1])
    #print(a[16][2])
    #print(a[17][

=======
Suggestion 8

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    l.sort()
    cnt = 1
    for i in range(n-1):
        if l[i] != l[i+1]:
            cnt += 1
    print(cnt)

=======
Suggestion 9

def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(list(map(int,input().split())))
    L.sort()
    #print(L)
    cnt = 1
    for i in range(N-1):
        if L[i] != L[i+1]:
            cnt += 1
    print(cnt)

=======
Suggestion 10

def main():
    N = int(input())
    L = [0] * N
    A = [0] * N
    for i in range(N):
        L[i], *A[i] = map(int, input().split())
    A.sort()
    ans = 1
    for i in range(1, N):
        if A[i] != A[i-1]:
            ans += 1
    print(ans)
