Synthesizing 10/10 solutions

=======
Suggestion 1

def S(n):
    return sum([int(i) for i in str(n)])

K = int(input())

=======
Suggestion 2

def S(n):
    return sum(map(int, list(str(n))))

=======
Suggestion 3

def main():
    k = int(input())
    i = 1
    while k > 0:
        if i % sum(map(int, str(i))) == 0:
            print(i)
            k -= 1
        i += 1

main()

=======
Suggestion 4

def S(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

=======
Suggestion 5

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

K = int(input())
n = 1
ans = []
while True:
    if S(n) * (n // S(n)) <= 10 ** 15:
        ans.append(S(n) * (n // S(n)))
    else:
        break
    n += 1
print(*sorted(ans)[:K], sep="\n")

=======
Suggestion 6

def s(n):
    return sum([int(i) for i in str(n)])

k = int(input())
n = 1
while k > 0:
    if n % s(n) == 0:
        print(n)
        k -= 1
    n += 1

=======
Suggestion 7

def s(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s

K = int(input())
n = 1
while K > 0:
    if n % s(n) == 0:
        print(n)
        K -= 1
    n += 1

=======
Suggestion 8

def S(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

K = int(input())

ans = []
n = 1
while len(ans) < K:
    if n // S(n) > 1:
        ans.append(n)
    n += 1

for a in ans:
    print(a)

=======
Suggestion 9

def snuke_number(k):
    i = 1
    while True:
        if i % sum(map(int, str(i))) == 0:
            k -= 1
            if k == 0:
                return i
        i += 1

=======
Suggestion 10

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
