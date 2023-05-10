Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, k = map(int, input().split())
    ans = []
    for i in range(1, 101):
        if a % i == 0 and b % i == 0:
            ans.append(i)
    print(ans[-k])

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b, k = map(int, input().split())
cnt = 0
for i in range(100, 0, -1):
    if a % i == 0 and b % i == 0:
        cnt += 1
        if cnt == k:
            print(i)
            break

=======
Suggestion 3

def main():
    a, b, k = map(int, input().split())
    cnt = 0
    for i in range(100, 0, -1):
        if a % i == 0 and b % i == 0:
            cnt += 1
            if cnt == k:
                print(i)
                break

=======
Suggestion 4

def main():
    a,b,k = map(int,input().split())
    cnt = 0
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            cnt += 1
            if cnt == k:
                print(i)
                break

=======
Suggestion 5

def common_divisor(a,b):
    # A,Bの最大公約数を求める
    while b:
        a,b = b,a%b
    return a

a,b,k = map(int,input().split())
c = common_divisor(a,b)
l = []

for i in range(1,c+1):
    if c % i == 0:
        l.append(i)

print(l[-k])

=======
Suggestion 6

def main():
    A, B, K = map(int, input().split())
    count = 0
    for i in range(1, 101):
        if A % i == 0 and B % i == 0:
            count += 1
            if count == K:
                print(i)
                break

=======
Suggestion 7

def main():
    A, B, K = map(int, input().split())
    divisors = []
    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            divisors.append(i)
    print(divisors[-K])

=======
Suggestion 8

def main():
    a, b, k = map(int, input().split())
    c = []
    for i in range(1, 101):
        if a % i == 0 and b % i == 0:
            c.append(i)
    print(c[-k])

=======
Suggestion 9

def main():
    a, b, k = map(int, input().split())

    count = 0
    for i in range(100, 0, -1):
        if a % i == 0 and b % i == 0:
            count += 1
            if count == k:
                print(i)
                exit()

=======
Suggestion 10

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
