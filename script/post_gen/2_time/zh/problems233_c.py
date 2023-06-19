Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,x = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(a[i][0]):
            if x % a[i][j + 1] == 0:
                for k in range(n):
                    if a[k][0] > 1 and a[k][1] * a[i][j + 1] == x:
                        ans += a[k][0] - 1
                    elif a[k][0] == 1 and a[k][1] == x // a[i][j + 1]:
                        ans += 1
    print(ans)

=======
Suggestion 2

def get_divisor(num):
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
    return divisors

n, x = map(int, input().split())
bags = []
for i in range(n):
    bags.append(list(map(int, input().split())))

divisors = get_divisor(x)
ans = 0
for divisor in divisors:
    for bag in bags:
        for ball in bag[1:]:
            if ball == divisor:
                ans += 1
                break
print(ans)

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(1, 1 << n):
        tmp = 1
        for j in range(n):
            if i >> j & 1:
                for k in range(a[j][0]):
                    tmp *= a[j][k + 1]
        if tmp == x:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    N,X = map(int, input().split())
    L = []
    a = []
    for i in range(N):
        L.append(list(map(int, input().split())))
        a.append(L[i][1:])
    print(L)
    print(a)

=======
Suggestion 6

def get_list():
    n_x = input()
    n_x = n_x.split(' ')
    n = int(n_x[0])
    x = int(n_x[1])
    bag = []
    for i in range(n):
        bag.append(input())
    return n,x,bag

=======
Suggestion 7

def get_divisors(n):
    divisors = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
        i += 1
    divisors.sort()
    return divisors

=======
Suggestion 8

def main():
    N,X = map(int,input().split())
    L = []
    for i in range(N):
        L.append(list(map(int,input().split())))

    #print(N,X)
    #print(L)
    #print(L[0][0])
    #print(L[0][1])
    #print(L[0][2])
    #print(L[1][0])
    #print(L[1][1])
    #print(L[1][2])

    #print(L[0][0]*L[1][0])
    #print(L[0][0]*L[1][1])
    #print(L[0][0]*L[1][2])
    #print(L[0][1]*L[1][0])
    #print(L[0][1]*L[1][1])
    #print(L[0][1]*L[1][2])
    #print(L[0][2]*L[1][0])
    #print(L[0][2]*L[1][1])
    #print(L[0][2]*L[1][2])

    #print(L[0][0]*L[1][0]*L[2][0])
    #print(L[0][0]*L[1][0]*L[2][1])
    #print(L[0][0]*L[1][0]*L[2][2])
    #print(L[0][0]*L[1][1]*L[2][0])
    #print(L[0][0]*L[1][1]*L[2][1])
    #print(L[0][0]*L[1][1]*L[2][2])
    #print(L[0][0]*L[1][2]*L[2][0])
    #print(L[0][0]*L[1][2]*L[2][1])
    #print(L[0][0]*L[1][2]*L[2][2])

    #print(L[0][1]*L[1][0]*L[2][0])
    #print(L[0][1]*L[1][0]*L[2][1])
    #print(L[0][1]*L[1][0]*L[2][2])
    #print(L[0][1]*L[1][1
