Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    result = [0] * N
    for i in range(N):
        for j in range(i + 1, N):
            if A[i] < A[j]:
                result[i] += 1
    for i in range(N):
        print(result[i])

solve()

=======
Suggestion 2

def problems273_c():
    pass

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    ans = [0] * n
    for i in range(n-1, -1, -1):
        if a[i] != a[i+1]:
            ans[i] = ans[i+1] + 1
        else:
            ans[i] = ans[i+1]
    for i in range(n):
        print(ans[i])

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    count = [0 for _ in range(N)]
    for i in range(N):
        for j in range(N-1):
            if A[j] > A[i]:
                count[i] += 1
    #print(count)
    for i in range(N):
        print(count.count(i))

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    a.append(0)
    count = 0
    ans = [0] * n
    for i in range(n):
        if a[i] != a[i + 1]:
            ans[count] = i + 1
            count += 1
    for i in range(n):
        print(ans[i])

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n)
    #print(a)
    a.sort()
    #print(a)
    #print(a[0])
    #print(a[n-1])
    #print(a[n-1] - a[0])
    #print(a[n-1] - a[0] + 1)
    #print(len(a))
    #print(len(set(a)))
    #print(set(a))
    #print(sorted(list(set(a))))
    #print(sorted(list(set(a)))[1])
    #print(sorted(list(set(a)))[2])
    #print(sorted(list(set(a)))[3])
    #print(sorted(list(set(a)))[4])
    #print(sorted(list(set(a)))[5])
    #print(sorted(list(set(a)))[6])
    #print(sorted(list(set(a)))[7])
    #print(sorted(list(set(a)))[8])
    #print(sorted(list(set(a)))[9])
    #print(sorted(list(set(a)))[10])
    #print(sorted(list(set(a)))[11])
    #print(sorted(list(set(a)))[12])
    #print(sorted(list(set(a)))[13])
    #print(sorted(list(set(a)))[14])
    #print(sorted(list(set(a)))[15])
    #print(sorted(list(set(a)))[16])
    #print(sorted(list(set(a)))[17])
    #print(sorted(list(set(a)))[18])
    #print(sorted(list(set(a)))[19])
    #print(sorted(list(set(a)))[20])
    #print(sorted(list(set(a)))[21])
    #print(sorted(list(set(a)))[22])
    #print(sorted(list(set(a)))[23])
    #print(sorted(list(set(a)))[24])
    #print(sorted(list(set(a)))[25])
    #print(sorted(list(set(a)))[26])
    #print(sorted(list(set(a)))[27])
    #print(sorted(list(set(a)))[28])
    #print(sorted(list(set(a)))[29])
    #print(sorted(list(set(a)))[30])
    #print(sorted(list(set(a)))[31])
    #print(sorted(list(set(a)))[32])
    #print(sorted(list(set(a)))[33])
    #print(sorted(list(set(a)))[34])
    #print(sorted(list(set(a)))[35])
    #print(sorted(list

=======
Suggestion 7

def solve(N, A):
    A.sort()
    ans = [0] * N
    for i in range(N):
        if i > 0 and A[i] == A[i-1]:
            ans[i] = ans[i-1]
            continue
        l = 0
        r = N
        while r - l > 1:
            m = (l + r) // 2
            if A[m] > A[i]:
                r = m
            else:
                l = m
        ans[i] = l
    return ans

N = int(input())
A = list(map(int, input().split()))
ans = solve(N, A)
for i in range(N):
    print(ans[i])

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    ans = [0] * n
    cnt = 1
    for i in range(n):
        if a[i] != a[i + 1]:
            for j in range(cnt, i + 1):
                ans[j] = cnt - 1
            cnt = i + 2
    print(*ans, sep='\n')

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * n
    for i in range(n):
        if i == 0:
            ans[i] = 1
        else:
            if a[i] == a[i-1]:
                ans[i] = ans[i-1]
            else:
                ans[i] = ans[i-1] + 1

    for i in range(n):
        print(ans[ans[i]-1])
