Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i]-1] += 1
    ans = 0
    for i in range(n):
        ans += b[i] * (b[i]-1) // 2
    for i in range(n):
        print(ans - (b[a[i]-1]-1))

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * n
    ans = [0] * n
    for i in range(n):
        cnt[a[i]-1] += 1
    for i in range(n):
        ans[i] = cnt[i] * (cnt[i]-1) // 2
    sum_ans = sum(ans)
    for i in range(n):
        print(sum_ans - ans[a[i]-1] + (cnt[a[i]-1]-1) * (cnt[a[i]-1]-2) // 2)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    cnt = [0]*(n+1)
    for i in range(1, n+1):
        cnt[a[i]] += 1
    ans = 0
    for i in range(1, n+1):
        ans += cnt[i]*(cnt[i]-1)//2
    for i in range(1, n+1):
        print(ans-cnt[a[i]]+1)

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    ans = 0
    cnt = 1
    for i in range(N):
        if A[i] != A[i+1]:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
        else:
            cnt += 1
    for i in range(N):
        if A[i] != A[i+1]:
            print(ans)
        else:
            print(ans - (cnt - 1))
solve()

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n + 1)
    for i in range(n):
        b[a[i]] += 1
    ans = 0
    for i in range(1, n + 1):
        ans += b[i] * (b[i] - 1) // 2
    for i in range(n):
        print(ans - b[a[i]] + 1)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print(len(A))
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])
    #print(A[10])
    #print(A[11])
    #print(A[12])
    #print(A[13])
    #print(A[14])
    #print(A[15])
    #print(A[16])
    #print(A[17])
    #print(A[18])
    #print(A[19])
    #print(A[20])
    #print(A[21])
    #print(A[22])
    #print(A[23])
    #print(A[24])
    #print(A[25])
    #print(A[26])
    #print(A[27])
    #print(A[28])
    #print(A[29])
    #print(A[30])
    #print(A[31])
    #print(A[32])
    #print(A[33])
    #print(A[34])
    #print(A[35])
    #print(A[36])
    #print(A[37])
    #print(A[38])
    #print(A[39])
    #print(A[40])
    #print(A[41])
    #print(A[42])
    #print(A[43])
    #print(A[44])
    #print(A[45])
    #print(A[46])
    #print(A[47])
    #print(A[48])
    #print(A[49])
    #print(A[50])
    #print(A[51])
    #print(A[52])
    #print(A[53])
    #print(A[54])
    #print(A[55])
    #print(A[56])
    #print(A[57])
    #print(A[58])
    #print(A[59])
    #print(A[60])
    #print(A[61])
    #print(A[62])
    #print(A[63])
    #print(A[64])
    #print(A[65])
    #print

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = [0]*(n+1)
    for i in range(n):
        b[a[i]] += 1
    s = 0
    for i in range(n+1):
        s += b[i]*(b[i]-1)//2
    for i in range(n):
        print(s-(b[a[i]]-1))

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans = sum([v*(v-1)//2 for v in d.values()])
    for i in a:
        print(ans - (d[i]-1))

=======
Suggestion 9

def get_value():
    N = int(input())
    A = list(map(int,input().split()))
    return N,A

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = {}
    for i in a:
        if i not in cnt:
            cnt[i] = 1
        else:
            cnt[i] += 1
    ans = 0
    for i in cnt:
        ans += cnt[i] * (cnt[i] - 1) // 2
    for i in a:
        print(ans - (cnt[i] - 1))
