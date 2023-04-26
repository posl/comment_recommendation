Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

=======
Suggestion 3

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n = int(input())
a = list(map(int,input().split()))

l = [0]*n
r = [0]*n

l[0] = a[0]
r[n-1] = a[n-1]

for i in range(1,n):
    l[i] = gcd(l[i-1],a[i])

for i in range(n-2,-1,-1):
    r[i] = gcd(r[i+1],a[i])

ans = 1

for i in range(n):
    if i == 0:
        ans = max(ans,r[i+1])
    elif i == n-1:
        ans = max(ans,l[i-1])
    else:
        ans = max(ans,gcd(l[i-1],r[i+1]))

print(ans)

=======
Suggestion 4

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

N = int(input())
A = list(map(int,input().split()))
L = [0]*(10**6+1)
for i in range(N):
    L[A[i]] += 1
for i in range(2,10**6+1):
    c = 0
    for j in range(i,10**6+1,i):
        c += L[j]
    if c > 1:
        break
else:
    print(0)
    exit()
for i in range(i,0,-1):
    c = 0
    for j in range(i,10**6+1,i):
        c += L[j]
    if c > 1:
        break
print(i)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] == a[i-1]:
            continue
        for j in range(i+1, n):
            if a[j] % a[i] == 0:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_a = max(a)
    max_a_divisors = [0] * (max_a + 1)
    for i in range(n):
        max_a_divisors[a[i]] += 1
    ans = 0
    for i in range(1, max_a + 1):
        if max_a_divisors[i] == 1:
            for j in range(i * 2, max_a + 1, i):
                max_a_divisors[j] = 0
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    max_a = max(a)
    div = [0] * (max_a + 1)
    for i in range(n):
        div[a[i]] += 1
    ans = 0
    for i in range(1, max_a + 1):
        if div[i] == 0:
            continue
        if div[i] == 1:
            ans += 1
            continue
        if div[i] >= 2:
            ans += 1
            for j in range(i * 2, max_a + 1, i):
                div[j] = 0
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_a = max(a)
    cnt = 0
    ans = [0] * (max_a + 1)

    for i in range(n):
        ans[a[i]] += 1

    for i in range(1, max_a + 1):
        if ans[i] == 1:
            cnt += 1

    print(cnt)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    max_num = A[-1]
    check = [True] * (max_num + 1)
    for i in range(N):
        if check[A[i]] == True:
            for j in range(2, max_num // A[i] + 1):
                check[j * A[i]] = False
    ans = 0
    for i in range(N):
        if check[A[i]] == True:
            ans += 1
    print(ans)

=======
Suggestion 10

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    maxA = max(A)
    A = set(A)
    ans = 0
    for i in range(1, maxA + 1):
        flag = True
        for j in range(2, maxA // i + 1):
            if i * j in A:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
    return 0
