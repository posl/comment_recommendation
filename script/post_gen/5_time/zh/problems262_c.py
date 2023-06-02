Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n, a)
    b = [0] * (n+1)
    for i in range(n):
        if a[i] > n:
            continue
        b[a[i]] += 1
    ans = 0
    for i in range(1, n+1):
        if b[i] == 0:
            continue
        ans += b[i] * (b[i]-1) // 2
    print(ans)

=======
Suggestion 2

def problems262_c():
    n = int(input())
    a = list(map(int, input().split()))
    l = [0]*(n+1)
    r = [0]*(n+1)
    for i in range(n):
        l[max(a[i], i+1)] += 1
        r[min(a[i], i+1)] += 1
    ans = 0
    for i in range(1, n+1):
        ans += l[i]*r[i]
    print(ans)

=======
Suggestion 3

def f(x):
    if x==0:
        return 0
    else:
        return x*(x-1)/2

N=int(raw_input())
a=map(int,raw_input().split())
b=[0]*N
for i in range(N):
    b[a[i]-1]=i
ans=0
for i in range(N):
    if i==0:
        if b[i]>b[i+1]:
            ans+=1
    elif i==N-1:
        if b[i]>b[i-1]:
            ans+=1
    else:
        if b[i]>b[i-1] and b[i]>b[i+1]:
            ans+=1
print ans

=======
Suggestion 4

def solve(n, a):
    ans = 0
    for i in range(n):
        if a[i] > i+1:
            continue
        if i+1 < a[a[i]-1]:
            continue
        if i+1 == a[a[i]-1]:
            ans += 1
    return ans

=======
Suggestion 5

def findMin(a, i):
    mini = a[i]
    minIndex = i
    for j in range(i+1, len(a)):
        if a[j] < mini:
            mini = a[j]
            minIndex = j
    return minIndex

=======
Suggestion 6

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    ans = 0
    for i in range(1, n):
        if b[i - 1] > b[i]:
            ans += 1
    print(ans)

=======
Suggestion 7

def solve(n, a):
    ans = 0
    for i in range(1, n):
        if a[i] > a[i - 1]:
            ans += 1
    return (ans + 1) * 2

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    l = [0]*(n+1)
    for i in range(n):
        l[a[i]] = i+1
    ans = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if l[i] > l[j]:
                break
            if l[i] < l[j] and l[j] < j:
                ans += 1
    print(ans)

=======
Suggestion 10

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    # print(n)
    # print(a)
    # print(len(a))
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if min(a[i], a[j]) == i+1 and max(a[i], a[j]) == j+1:
                cnt += 1
    print(cnt)

solve()
