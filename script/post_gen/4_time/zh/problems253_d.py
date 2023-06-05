Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, a, b = map(int, input().split())
    print(sum(i for i in range(1, n+1) if i % a != 0 and i % b != 0))

=======
Suggestion 2

def gcd(a,b):
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

=======
Suggestion 3

def solve(num, a, b):
    sum = 0
    for i in range(1, num+1):
        if i % a != 0 and i % b != 0:
            sum += i
    return sum

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N, a, b = map(int, input().split())
g = gcd(a, b)
lcm = a * b // g
print((N // a + N // b - N // lcm) * (N + 1) - N)

=======
Suggestion 5

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 6

def get_sum(n, a, b):
    sum = 0
    for i in range(1, n+1):
        if i % a != 0 and i % b != 0:
            sum += i
    return sum

=======
Suggestion 7

def main():
    N, A, B = map(int, input().split())
    #print(N, A, B)
    sum = 0
    for i in range(1, N+1):
        if (i % A != 0) and (i % B != 0):
            sum += i
    print(sum)

main()

=======
Suggestion 8

def main():
    n,a,b = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        if i%a!=0 and i%b!=0:
            ans += i
    print(ans)
