Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

=======
Suggestion 2

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 3

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a,b,k=map(int,input().split())
g=gcd(a,b)
lcm=a*b//g
ans=0
for i in range(lcm,0,-1):
    if a%i==0 and b%i==0:
        k-=1
        if k==0:
            ans=i
            break
print(ans)

=======
Suggestion 4

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a,b,k=map(int,input().split())
c=gcd(a,b)
count=0
for i in range(c,0,-1):
    if a%i==0 and b%i==0:
        count+=1
    if count==k:
        print(i)
        break

=======
Suggestion 5

def func(a,b,k):
    c=a*b
    d=c//a
    e=c//b
    f=d+e
    g=f//2
    h=g//k
    return h
a,b,k=map(int,input().split())
print(func(a,b,k))

=======
Suggestion 6

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

=======
Suggestion 7

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a, b, k = map(int, input().split())
gcd = gcd(a, b)
gcd_list = []
for i in range(1, gcd + 1):
    if gcd % i == 0:
        gcd_list.append(i)
print(gcd_list[-k])

=======
Suggestion 8

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

A, B, K = map(int, input().split())
# 1から100までの整数を格納するリスト
list = []
# 1から100までの整数をリストに格納する
for i in range(1, 101):
    list.append(i)
# 降順にソートする
list.sort(reverse=True)
# 答えを格納する変数
ans = 0
# 入力されたAとBの最大公約数を求める
gcd = gcd(A, B)
# 最大公約数であまりが0となるものをリストから削除する
for i in range(len(list)):
    if list[i] % gcd == 0:
        list[i] = 0
# 降順にソートする
list.sort(reverse=True)
# 0を削除する
while 0 in list:
    list.remove(0)
# K番目を求める
ans = list[K - 1]
print(ans)

=======
Suggestion 9

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b, k = map(int, input().split())
c = gcd(a, b)
ans = 1
for i in range(c, 0, -1):
    if c % i == 0:
        k -= 1
        if k == 0:
            ans = i
            break
print(ans)

=======
Suggestion 10

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a,b,k=map(int,input().split())
g=gcd(a,b)
l=[]
for i in range(1,g+1):
    if g%i==0:
        l.append(i)
print(l[-k])
