Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def divisors(n):
    i = 1
    table = []
    while i*i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    table.sort()
    return table

N = int(input())

ans = divisors(N)

for i in ans:
    print(i)

=======
Suggestion 2

def main():
    n = int(input())
    ans = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ans.add(i)
            ans.add(n//i)
    for i in sorted(ans):
        print(i)

=======
Suggestion 3

def main():
    n = int(input())
    i = 1
    ans = []
    while i * i <= n:
        if n % i == 0:
            ans.append(i)
            if i != n // i:
                ans.append(n // i)
        i += 1
    ans.sort()
    for a in ans:
        print(a)

=======
Suggestion 4

def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)
    divisors.sort()
    return divisors
 
N = int(input())
print(*divisors(N), sep='\n')

=======
Suggestion 5

def main():
    n = int(input())
    ans = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ans.add(i)
            ans.add(n // i)
    for i in sorted(ans):
        print(i)
main()

=======
Suggestion 6

def divisors(n):
    d = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            d.append(i)
            if i*i != n:
                d.append(n//i)
        i += 1
    d.sort()
    return d

N = int(input())
d = divisors(N)
for i in range(len(d)):
    print(d[i])

=======
Suggestion 7

def solve(n):
    ans = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ans.append(i)
            if i != n // i:
                ans.append(n // i)
    ans.sort()
    return ans

=======
Suggestion 8

def get_divisor(n):
    divisor = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            divisor.append(i)
            if i != n//i:
                divisor.append(n//i)
    divisor.sort()
    return divisor

n = int(input())
divisor = get_divisor(n)
for i in divisor:
    print(i)

=======
Suggestion 9

def solve():
    N = int(input())
    ans = []
    for i in range(1, int(N**0.5)+1):
        if N%i == 0:
            ans.append(i)
            if N//i != i:
                ans.append(N//i)
    ans.sort()
    for i in ans:
        print(i)
