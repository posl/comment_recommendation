Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 2

def main():
    a, b, k = map(int, input().split())
    c = []
    for i in range(1, 101):
        if a % i == 0 and b % i == 0:
            c.append(i)
    print(c[-k])

=======
Suggestion 3

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a,b,k = map(int,input().split())
count = 0
for i in range(100,0,-1):
    if a%i==0 and b%i==0:
        count += 1
    if count == k:
        print(i)
        break

=======
Suggestion 4

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

=======
Suggestion 5

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

a,b,k = map(int,input().split())

g = gcd(a,b)

l = []
for i in range(1,g+1):
    if g%i == 0:
        l.append(i)

print(l[-k])

=======
Suggestion 6

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a,b,k=map(int,input().split())
c=gcd(a,b)
d=1
for i in range(c,0,-1):
    if c%i==0:
        d+=1
    if d==k+1:
        print(i)
        break

=======
Suggestion 7

def divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

=======
Suggestion 8

def main():
    a, b, k = map(int, input().split())
    d = []
    for i in range(1, 101):
        if a % i == 0 and b % i == 0:
            d.append(i)
    print(d[-k])

=======
Suggestion 9

def main():
    a, b, k = map(int, input().split())
    count = 0
    for i in range(1, 101):
        if a % i == 0 and b % i == 0:
            count += 1
            if count == k:
                print(i)
                break
