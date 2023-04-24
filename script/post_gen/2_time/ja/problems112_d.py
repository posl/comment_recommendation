Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

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
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 4

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    print(M // N)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())

    # M が N で割り切れる場合
    if M % N == 0:
        print(M // N)
    # M が N で割り切れない場合
    else:
        print(M // N)

=======
Suggestion 7

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

N,M=map(int,input().split())
a=[]
for i in range(1,M//N+1):
    a.append(i)
#print(a)
ans=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        ans=max(ans,gcd(a[i],a[j]))
print(ans)

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    print(m // n)

=======
Suggestion 9

def main():
    # 整数の入力
    N,M = map(int,input().split())
    # 出力
    print(M//N)
