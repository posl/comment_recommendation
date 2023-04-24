Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
g = gcd(a, b)
ans = 0
for i in range(1, int(g**0.5)+1):
    if g % i == 0:
        ans += 2

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 3

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 5

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    ans = 1
    for i in range(2,min(a,b)+1):
        if a%i==0 and b%i==0:
            ans += 1
    print(ans)

=======
Suggestion 7

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

a, b = map(int, input().split())
d = gcd(a, b)
ans = 1
for i in range(2, int(d**0.5)+1):
    if d % i == 0:
        ans += 1
        if i != d // i:
            ans += 1
print(ans)

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    c = 1
    for i in range(2, a+1):
        if a%i==0 and b%i==0:
            c += 1
    print(c)

=======
Suggestion 9

def main():
    A, B = map(int, input().split())
    #AとBの最大公約数を求める
    def gcd(a, b):
        if a%b == 0:
            return b
        else:
            return gcd(b, a%b)
    #AとBの最大公約数を求める
    G = gcd(A, B)
    #Gの約数を求める
    def divisor(n):
        i = 1
        table = []
        while i*i <= n:
            if n%i == 0:
                table.append(i)
                if i != n//i:
                    table.append(n//i)
            i += 1
        return table
    #Gの約数の個数を求める
    print(len(divisor(G)))
