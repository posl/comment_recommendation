Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int,input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    l = sorted(d.items(), key=lambda x:x[1], reverse=True)
    s = 0
    for i in range(n):
        if l[i][1] == 1:
            break
        s += 1
    for i in range(n):
        if l[i][1] == 1:
            print(s)
        else:
            print(s+1)

=======
Suggestion 2

def solve():
    from collections import defaultdict
    N = int(input())
    A = list(map(int, input().split()))
    B = defaultdict(int)
    for a in A:
        B[a] += 1
    C = [0] * N
    for i in B:
        C[B[i]-1] += 1
    for i in C:
        print(i)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    ans = [0] * N
    cnt = 1
    for i in range(N):
        if A[i] != A[i+1]:
            ans[cnt-1] += 1
            cnt = 1
        else:
            cnt += 1
    print(*ans, sep="\n")

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * n
    cnt = 0
    for i in range(n):
        if i != 0 and a[i-1] != a[i]:
            ans[cnt] += 1
            cnt = 0
        else:
            cnt += 1
    ans[cnt] += 1
    for i in range(n):
        print(ans[i])

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    a.append(0)
    ans = 0
    cnt = 1
    for i in range(n):
        if a[i] == a[i+1]:
            cnt += 1
        else:
            ans += n - cnt
            cnt = 1
    for i in range(n):
        print(ans - (n - i - 1))

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    i = 0
    j = 0
    count = 0
    ans = [0] * N
    while i < N:
        if A[i] == A[j]:
            count += 1
            i += 1
        else:
            ans[count - 1] += 1
            count = 0
            j = i
    ans[count - 1] += 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    ans = [0] * N
    ans[0] = 1
    count = 0
    for i in range(N):
        if A[i] != A[i+1]:
            ans[count] += 1
            count = 0
        else:
            count += 1
    print("\n".join(map(str, ans)))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    #print(A)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()

    ans = 0
    cnt = 0
    for i in range(n):
        if i == 0:
            ans += 1
        elif a[i] != a[i-1]:
            ans += 1
            cnt = 0
        else:
            cnt += 1
            if cnt == ans:
                ans += 1
                cnt = 0
    for i in range(n):
        print(ans)

=======
Suggestion 10

def main():
    N=int(input())
    A=list(map(int,input().split()))
    A.sort()
    #print(A)
    #print(A[-1])
    #print(A[-2])
    #print(A[-3])
    #print(A[-4])
    #print(A[-5])
    #print(A[-6])
    #print(A[-7])
    #print(A[-8])
    #print(A[-9])
    #print(A[-10])
    #print(A[-11])
    #print(A[-12])
    #print(A[-13])
    #print(A[-14])
    #print(A[-15])
    #print(A[-16])
    #print(A[-17])
    #print(A[-18])
    #print(A[-19])
    #print(A[-20])
    #print(A[-21])
    #print(A[-22])
    #print(A[-23])
    #print(A[-24])
    #print(A[-25])
    #print(A[-26])
    #print(A[-27])
    #print(A[-28])
    #print(A[-29])
    #print(A[-30])
    #print(A[-31])
    #print(A[-32])
    #print(A[-33])
    #print(A[-34])
    #print(A[-35])
    #print(A[-36])
    #print(A[-37])
    #print(A[-38])
    #print(A[-39])
    #print(A[-40])
    #print(A[-41])
    #print(A[-42])
    #print(A[-43])
    #print(A[-44])
    #print(A[-45])
    #print(A[-46])
    #print(A[-47])
    #print(A[-48])
    #print(A[-49])
    #print(A[-50])
    #print(A[-51])
    #print(A[-52])
    #print(A[-53])
    #print(A[-54])
    #print(A[-55])
    #print(A[-56])
    #print(A[-57])
    #print(A[-58])
    #print(A[-59])
    #print(A[-60])
    #print(A[-61])
    #print(A[-62])
    #print(A[-63])
    #print(A[-64])
    #print(A[-65])
    #print(A[-66])
    #print(A[-67])
    #print(A[-68
