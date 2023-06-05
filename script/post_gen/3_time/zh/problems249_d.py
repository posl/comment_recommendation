Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

N = int(input())
A = list(map(int,input().split()))
ans = 0

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))
cnt = 0
d = {}
for i in range(n):
    for j in range(i + 1, n):
        g = gcd(a[i], a[j])
        if g == 1:
            continue
        if g in d:
            d[g] += 1
        else:
            d[g] = 1
        if a[i] // g in d:
            cnt += d[a[i] // g]
print(cnt)

=======
Suggestion 3

def main():
    # input
    n = int(input())
    a_list = list(map(int, input().split()))
    # solve
    ans = 0
    d = {}
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a_list[j] == 0:
                continue
            if a_list[i] % a_list[j] != 0:
                continue
            if a_list[i] // a_list[j] in d:
                ans += d[a_list[i] // a_list[j]]
    # output
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    for i in range(n):
        for j in range(n):
            if a[j] == 0:
                continue
            if a[i] % a[j] == 0:
                x = a[i] // a[j]
                if x in d:
                    ans += d[x]
    print(ans)

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
a = list(map(int, input().split()))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    cnt = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if a[i] % a[j] == 0:
                cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = {}

    for i in range(n):
        c[a[i]] = c.get(a[i], 0) + 1

    ans = 0
    for i in range(n):
        for j in range(n):
            if a[i] == 0:
                continue
            if a[j] == 0:
                continue
            if a[i] % a[j] != 0:
                continue
            if c.get(a[i] // a[j], 0) == 0:
                continue
            ans += c[a[i] // a[j]]

    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    d = {}
    for i in range(1, n+1):
        if a[i] not in d.keys():
            d[a[i]] = 1
        else:
            d[a[i]] += 1
    ans = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if a[i] % a[j] != 0:
                continue
            if a[i] // a[j] not in d.keys():
                continue
            ans += d[a[i] // a[j]]
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cnt = [0] * (max(a) + 1)
    for i in range(n):
        cnt[a[i]] += 1
    for i in range(n):
        for j in range(1, int(a[i] ** 0.5) + 1):
            if a[i] % j == 0:
                if j * j == a[i]:
                    ans += cnt[j] * (cnt[j] - 1)
                else:
                    ans += cnt[j] * cnt[a[i] // j]
    print(ans // 2)

main()

=======
Suggestion 10

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a
