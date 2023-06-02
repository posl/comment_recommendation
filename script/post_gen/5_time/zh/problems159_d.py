Synthesizing 10/10 solutions

=======
Suggestion 1

def cal(nums):
    n = len(nums)
    if n < 2:
        return 0
    nums.sort()
    i = 0
    j = 1
    count = 0
    while i < n and j < n:
        if nums[i] == nums[j]:
            count += 1
            j += 1
        elif nums[i] < nums[j]:
            i += 1
            j += 1
        else:
            i += 1
    return count

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (n+1)
    for i in range(n):
        cnt[a[i]] += 1
    ans = sum([i*(i-1)//2 for i in cnt])
    for i in range(n):
        print(ans - cnt[a[i]] + 1)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    ans = [0] * N
    count = 1
    for i in range(N):
        if A[i] == A[i + 1]:
            count += 1
        else:
            ans[A[i] - 1] = count
            count = 1
    for i in range(N):
        print(N - ans[i])
main()

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * (n + 1)
    for i in range(n):
        if i == 0:
            b[i] = 1
            continue
        if a[i] == a[i - 1]:
            b[i] = b[i - 1] + 1
        else:
            b[i] = 1
    ans = 0
    for i in range(n):
        ans += b[i] * (b[i] - 1) // 2
    for i in range(n):
        if a[i] != a[i - 1]:
            continue
        ans -= (b[i] - 1) * (b[i] - 2) // 2
    for i in range(n):
        if a[i] == a[i - 1]:
            continue
        ans -= (b[i] - 1) * (b[i] - 2) // 2
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(x) for x in input().split()]

    count = [0] * (N + 1)
    for i in range(N):
        count[A[i]] += 1

    total = 0
    for i in range(1, N + 1):
        total += count[i] * (count[i] - 1) // 2

    for i in range(N):
        print(total - count[A[i]] + 1)

=======
Suggestion 6

def cal(a):
    return a*(a-1)//2

n=int(input())
a=list(map(int,input().split()))
d={}
for i in range(n):
    if a[i] not in d:
        d[a[i]]=1
    else:
        d[a[i]]+=1
s=sum(list(map(cal,d.values())))
for i in range(n):
    print(s-(d[a[i]]-1))

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    d = {}
    for i in range(n):
        d[i+1] = 0
    for i in range(n):
        d[a[i]] += 1
    print(d)
    for i in range(n):
        print(n - d[a[i]] + 1)

=======
Suggestion 8

def main():
    n = int(input())
    a = [0] * n
    for i, x in enumerate(map(int, input().split())):
        a[x - 1] += 1
    s = sum(x * (x - 1) // 2 for x in a)
    for x in a:
        print(s - x * (x - 1) // 2 + (x - 1) * (x - 2) // 2)

=======
Suggestion 9

def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=[0]*(n+1)
    for i in range(n):
        b[a[i]]+=1
    ans=[0]*(n+1)
    for i in range(1,n+1):
        ans[i]=ans[i-1]+b[i]*(b[i]-1)//2
    for i in range(n):
        print(ans[a[i]])

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n+1)
    for i in a:
        b[i] += 1
    ans = 0
    for i in range(1, n+1):
        ans += b[i] * (b[i]-1) // 2
    for i in a:
        print(ans - (b[i]-1))
