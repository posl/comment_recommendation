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

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a

=======
Suggestion 3

def main():
    a, b, k = map(int, input().split())
    count = 0
    for i in range(1, max(a, b) + 1):
        if a % i == 0 and b % i == 0:
            count += 1
            if count == k:
                print(i)
                exit()

=======
Suggestion 4

def get_common_multiple(A,B,K):
    #A,B,K = map(int,input().split())
    #print(A,B,K)
    #print(A,B,K)
    #print(type(A))
    #print(type(B))
    #print(type(K))
    #print(type(A*B))
    #print(type(A*B/K))
    #print(type(A*B//K))
    #print(type(int(A*B/K)))
    #print(type(int(A*B//K)))
    #print(A*B/K)
    #print(A*B//K)
    #print(int(A*B/K))
    #print(int(A*B//K))
    #print(A*B%K)
    #print(A*B//K+1)
    if A*B%K == 0:
        return int(A*B//K)
    else:
        return int(A*B//K+1)

=======
Suggestion 5

def main():
    a,b,k = map(int,input().split())
    array = []
    for i in range(1,101):
        if a % i == 0 and b % i == 0:
            array.append(i)
    print(array[-k])

=======
Suggestion 6

def problem120_b():
    a,b,k = map(int,input().split())
    res = []
    for i in range(1,101):
        if a%i==0 and b%i==0:
            res.append(i)
    print(res[-k])

=======
Suggestion 7

def main():
    a, b, k = map(int, input().split())
    count = 0
    for i in range(100, 0, -1):
        if a % i == 0 and b % i == 0:
            count += 1
            if count == k:
                print(i)
                break

=======
Suggestion 8

def main():
    a,b,k = map(int,input().split())
    count = 0
    for i in range(1,101):
        if a%i == 0 and b%i == 0:
            count += 1
            if count == k:
                print(i)
                break

=======
Suggestion 9

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b, k = map(int, input().split())
g = gcd(a, b)
cnt = 0
for i in range(g, 0, -1):
    if g % i == 0:
        cnt += 1
        if cnt == k:
            print(i)
            break
