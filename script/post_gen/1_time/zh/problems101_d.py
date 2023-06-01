Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def S(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

K = int(input())
n = 0
while K > 0:
    n += 1
    if n % S(n) == 0:
        K -= 1
print(n)

=======
Suggestion 2

def S(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s

=======
Suggestion 3

def s(n):
    return sum([int(i) for i in str(n)])

=======
Suggestion 4

def S(n):
    a = str(n)
    sum = 0
    for i in a:
        sum += int(i)
    return sum

K = int(input())
n = 1
for i in range(K):
    while S(n) * K != S(n * K):
        n += 1
    print(n)
    n += 1

=======
Suggestion 5

def main():
    K = int(input())
    n = 1
    while K > 0:
        if n % sum([int(i) for i in str(n)]) == 0:
            print(n)
            K -= 1
        n += 1

=======
Suggestion 6

def S(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

K = int(input())
snuke = []
n = 1
while len(snuke) < K:
    if n % S(n) == 0:
        snuke.append(n)
    n += 1
for i in range(K):
    print(snuke[i])

=======
Suggestion 7

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

K = int(input())
count = 0
n = 1
while count < K:
    if n % S(n) == 0:
        print(n)
        count += 1
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
i = 1
while K > 0:
    if i % S(i) == 0:
        print(i)
        K -= 1
    i += 1

=======
Suggestion 9

def S(n):
    return sum(map(int,str(n)))

k = int(input())
a = []
n = 0
while len(a) < k:
    n += 1
    if n % S(n) == 0:
        a.append(n)
print(*a,sep="\n")
