Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 2

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, m = map(int, input().split())
a = list(map(int, input().split()))
max_a = max(a)
gcd_a = [0] * (max_a + 1)
for i in range(n):
    for j in range(1, int(max_a ** 0.5) + 1):
        if a[i] % j == 0:
            gcd_a[j] = 1
            gcd_a[a[i] // j] = 1
ans = []
for i in range(1, m + 1):
    if gcd_a[i] == 0:
        ans.append(i)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])

=======
Suggestion 4

def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return gcd(y, x % y)

=======
Suggestion 5

def gcd(x, y):
    if x < y:
        x, y = y, x
    while x % y != 0:
        x, y = y, x % y
    return y

=======
Suggestion 6

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a

=======
Suggestion 7

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = []
for i in range(1, m + 1):
    flag = True
    for j in range(n):
        if gcd(a[j], i) != 1:
            flag = False
            break
    if flag:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i)
