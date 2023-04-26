Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    sum = 0
    for i in range(1, N+1):
        if i % 3 == 0 and i % 5 == 0:
            sum += i
        elif i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
        else:
            sum += i
    print(sum)
main()

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        if i%3==0 or i%5==0:
            continue
        else:
            ans += i
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        if i%3 == 0 and i%5 == 0:
            ans += 0
        elif i%3 == 0:
            ans += 0
        elif i%5 == 0:
            ans += 0
        else:
            ans += i
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    sum = 0
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            sum += 0
        elif i % 3 == 0:
            sum += 0
        elif i % 5 == 0:
            sum += 0
        else:
            sum += i
    print(sum)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i%3==0 and i%5==0:
            continue
        elif i%3==0 or i%5==0:
            continue
        else:
            ans += i
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        if i%15==0:
            ans += i
        elif i%3==0:
            ans += i
        elif i%5==0:
            ans += i
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                ans += 0
            else:
                ans += i
        else:
            if i % 5 == 0:
                ans += i
            else:
                ans += i
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    print(fizzbuzz(N))

=======
Suggestion 9

def main():
    N = int(input())
    # N = 15
    # N = 1000000
    # 3の倍数の和
    n_3 = N // 3
    sum_3 = (n_3 * (n_3 + 1)) // 2 * 3
    # 5の倍数の和
    n_5 = N // 5
    sum_5 = (n_5 * (n_5 + 1)) // 2 * 5
    # 15の倍数の和
    n_15 = N // 15
    sum_15 = (n_15 * (n_15 + 1)) // 2 * 15
    # 3の倍数と5の倍数の和
    print(sum_3 + sum_5 - sum_15)

=======
Suggestion 10

def main():
    N = int(input())
    print(calc(N))
