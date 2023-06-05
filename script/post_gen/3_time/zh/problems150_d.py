Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 2

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

=======
Suggestion 3

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lcm = a[0]
for i in range(1, n):
    lcm = a[i] * lcm // gcd(a[i], lcm)
for i in range(n):
    if (lcm // a[i]) % 2 == 0:
        print(0)
        exit()
lcm //= 2
ans = m // lcm
print((ans + 1) // 2)

=======
Suggestion 4

def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

=======
Suggestion 5

def gcd(x,y):
    if x<y:
        x,y=y,x
    if y==0:
        return x
    else:
        return gcd(y,x%y)

=======
Suggestion 6

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

=======
Suggestion 7

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

=======
Suggestion 8

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        temp = a % b
        a = b
        b = temp
    return a

n,m = map(int,input().split())
a = list(map(int,input().split()))
a = list(set(a))
a.sort()
ans = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]*a[j] > 2*m:
            break
        if gcd(a[i],a[j]) == a[i]:
            ans += 1
print(ans)

=======
Suggestion 9

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
