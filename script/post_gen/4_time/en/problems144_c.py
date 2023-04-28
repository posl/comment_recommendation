Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    count = 0
    while N > 1:
        if N % 2 == 0:
            N = N / 2
            count += 1
        else:
            N -= 1
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    while N > 1:
        if N % 2 == 0:
            N = N // 2
        else:
            N = N - 1
            ans += 1
    print(ans + 1)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    while N > 1:
        if N % 2 == 0:
            N = N // 2
        else:
            N = N - 1
        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    while(N > 1):
        if(N % 2 == 0):
            N = N / 2
        else:
            N = N - 1
        ans = ans + 1
    print(ans+1)

=======
Suggestion 5

def main():
    N = int(input())
    count = 0
    while N > 2:
        if N % 2 == 0:
            N = N // 2
        else:
            N -= 1
            count += 1
    print(count + 2)

=======
Suggestion 6

def main():
    n = int(input())
    m = int(n**0.5)
    if m*m == n:
        print(m*2-2)
    elif m*(m+1) >= n:
        print(m*2-1)
    else:
        print(m*2)

=======
Suggestion 7

def main():
    n = int(input())
    ans = 0
    while n > 0:
        ans += n % 2
        n //= 2
    print(ans)

=======
Suggestion 8

def main():
    # Take input Here and Call solution function
    n = int(input())
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n - 1
        count += 1
    print(count + 1)

=======
Suggestion 9

def main():
    n = int(input())
    for i in range(1, 10**6):
        if i*i > n:
            print((i-1)*2)
            break

=======
Suggestion 10

def solution(n):
    i = 1
    j = 1
    count = 0
    while i*j < n:
        if i*j*2 < n:
            if i < j:
                i += 1
            else:
                j += 1
        else:
            if i < j:
                j += 1
            else:
                i += 1
        count += 1
    return count

print(solution(10))
print(solution(50))
print(solution(10000000019))
