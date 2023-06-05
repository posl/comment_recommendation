Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

=======
Suggestion 2

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


n, m = map(int, input().split())
a = list(map(int, input().split()))
a = list(set(a))
a.sort()
lcm = a[0]
for i in range(1, len(a)):
    lcm = lcm * a[i] // gcd(lcm, a[i])
for i in range(len(a)):
    if (lcm // a[i]) % 2 == 0:
        print(0)
        exit()
ans = m // lcm
ans = (ans + 1) // 2
print(ans)

=======
Suggestion 3

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

=======
Suggestion 4

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 5

def gcd(a,b):
    if a < b:
        a,b = b,a
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n, m = map(int, input().split())
a = list(map(int, input().split()))
a = list(map(lambda x: x//2, a))
lcm = a[0]
for i in range(1, n):
    lcm = lcm * a[i] // gcd(lcm, a[i])
lcm = lcm // 2
ans = m // lcm
print(ans)
