Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, K = map(int, input().split())
    for i in range(min(A, B), 0, -1):
        if A % i == 0 and B % i == 0:
            K -= 1
        if K == 0:
            print(i)
            break

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

=======
Suggestion 3

def main():
    A, B, K = map(int, input().split())
    count = 0
    for i in range(1, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            count += 1
            if count == K:
                print(i)
                break

=======
Suggestion 4

def main():
    a, b, k = map(int, input().split())
    divs = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            divs.append(i)
    print(divs[-k])

=======
Suggestion 5

def get_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

=======
Suggestion 6

def main():
    A, B, K = map(int, input().split())
    count = 0
    for i in range(1, max(A,B)+1):
        if A % i == 0 and B % i == 0:
            count += 1
        if count == K:
            print(i)
            break

=======
Suggestion 7

def main():
    a,b,k = map(int,input().split())
    div = []
    for i in range(1,max(a,b)+1):
        if a%i == 0 and b%i == 0:
            div.append(i)
    print(div[-k])

=======
Suggestion 8

def main():
    a, b, k = map(int, input().split())
    common_divisors = []
    for i in range(1, min(a,b)+1):
        if a%i == 0 and b%i == 0:
            common_divisors.append(i)
    print(common_divisors[-k])

=======
Suggestion 9

def gcd(a,b):
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

=======
Suggestion 10

def main():
    a, b, k = map(int, input().split())
    c = min(a, b)
    ans = 0
    while c > 0:
        if a % c == 0 and b % c == 0:
            k -= 1
            if k == 0:
                ans = c
                break
        c -= 1
    print(ans)

main()
