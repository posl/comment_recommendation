Synthesizing 10/10 solutions

=======
Suggestion 1

def factors(n):
    return set(x for tup in ([i, n//i] 
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    L = []
    A = []
    for i in range(N):
        l, *a = map(int, input().split())
        L.append(l)
        A.append(a)
    ans = 0
    for i in range(1, 2**N):
        b = 0
        for j in range(N):
            if i >> j & 1:
                b += L[j]
        if b > X:
            continue
        for j in range(1, 2**b):
            c = 1
            for k in range(b):
                if j >> k & 1:
                    c *= A[k].pop()
            if c == X:
                ans += 1
    print(ans)

=======
Suggestion 3

def get_divisors(num):
    divisors = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)

    divisors.sort()
    return divisors

=======
Suggestion 4

def get_divisors(n):
    i = 1
    divisors = []
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    divisors.sort()
    return divisors

=======
Suggestion 5

def get_input():
    N, X = map(int, input().split())
    L = []
    A = []
    for i in range(N):
        l, *a = map(int, input().split())
        L.append(l)
        A.append(a)
    return N, X, L, A

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        ans += L[i][0]
    print(ans)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    bags = []
    for i in range(N):
        bags.append(list(map(int, input().split()))[1:])
    ans = 0
    for i in range(1, X + 1):
        if X % i == 0 and X // i <= 10**9:
            for bag in bags:
                if i in bag:
                    break
            else:
                continue
            for bag in bags:
                if X // i in bag:
                    ans += 1
                    break
    print(ans)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    ans = 0
    for i in range(2**N):
        tmp = 1
        for j in range(N):
            if i & 1<<j:
                tmp *= L[j][0]
        if tmp == X:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    n, x = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        if i == 0:
            ans = [a for a in l[i]]
        else:
            tmp = []
            for a in l[i]:
                for b in ans:
                    tmp.append(a*b)
            ans = tmp
    print(ans.count(x))

=======
Suggestion 10

def main():
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    L.sort(key=lambda x: x[0])
    #print(L)
    #print(N, X)
    ans = 0
    for i in range(N):
        for j in range(L[i][0]):
            if X % L[i][1+j] == 0:
                #print(L[i][1+j])
                if i == N-1:
                    ans += 1
                else:
                    X = X // L[i][1+j]
    print(ans)
    return
