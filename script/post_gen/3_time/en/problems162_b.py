Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if i % 3 != 0 and i % 5 != 0:
            ans += i
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        if i % 3 != 0 and i % 5 != 0:
            ans += i
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            continue
        ans += i
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            continue
        elif i % 3 == 0:
            continue
        elif i % 5 == 0:
            continue
        sum += i
    print(sum)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i%3 == 0 or i%5 == 0:
            continue
        ans += i
    print(ans)

main()

=======
Suggestion 6

def main():
    N = int(input())
    print((N // 3) * (1 + N // 3) * 3 // 2 + (N // 5) * (1 + N // 5) * 5 // 2 - (N // 15) * (1 + N // 15) * 15 // 2)

=======
Suggestion 7

def main():
    n = int(input())
    if n % 3 == 0:
        n3 = n // 3 - 1
    else:
        n3 = n // 3
    if n % 5 == 0:
        n5 = n // 5 - 1
    else:
        n5 = n // 5
    if n % 15 == 0:
        n15 = n // 15 - 1
    else:
        n15 = n // 15

    sum3 = 3 * n3 * (n3 + 1) // 2
    sum5 = 5 * n5 * (n5 + 1) // 2
    sum15 = 15 * n15 * (n15 + 1) // 2

    print(sum3 + sum5 - sum15)

main()

=======
Suggestion 8

def main():
    N = int(input())
    print((N//3)*(3+3*(N//3-1))//2 + (N//5)*(5+5*(N//5-1))//2 - (N//15)*(15+15*(N//15-1))//2)

=======
Suggestion 9

def solve():
    N = int(input())
    a = 0
    b = 0
    c = 0
    for i in range(1, N+1):
        if i % 3 == 0:
            a += i
        if i % 5 == 0:
            b += i
        if i % 15 == 0:
            c += i
    print(a+b-b)
