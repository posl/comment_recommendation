Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    i = 2
    while i*i <= N:
        while N%i == 0:
            N //= i
            ans += 1
        i += 1
    if N != 1:
        ans += 1
    print(ans)

main()

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    while N != 1:
        for i in range(2, N+1):
            if N % i == 0:
                N = N // i
                ans += 1
                break
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    while N > 1:
        for i in range(2, N+1):
            if N % i == 0:
                N //= i
                ans += 1
                break
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    z = 2
    count = 0
    while N != 1:
        if N % z == 0:
            N = N // z
            count += 1
        else:
            z += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(2, N+1):
        if N % i == 0:
            while N % i == 0:
                N = N // i
            ans += 1
    if N != 1:
        ans += 1
    print(ans)

=======
Suggestion 6

def main():
    import math
    N = int(input())
    ans = 0
    for p in range(2, int(math.sqrt(N))+1):
        while N % p == 0:
            N //= p
            ans += 1
    if N > 1:
        ans += 1
    print(ans)

=======
Suggestion 7

def main():
    import math
    N = int(input())
    ans = 0
    for i in range(2, math.floor(math.sqrt(N)) + 1):
        while N % i == 0:
            N //= i
            ans += 1
    if N > 1:
        ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    for p in range(2, 100000):
        if p*p > N:
            break
        if N % p != 0:
            continue
        e = 0
        while N % p == 0:
            N //= p
            e += 1
        ans += e
    if N > 1:
        ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    cnt = 0
    for p in range(2, N):
        if N % p == 0:
            cnt += 1
            N /= p
            while N % p == 0:
                N /= p
        if N == 1:
            break
    if N != 1:
        cnt += 1
    print(cnt)

=======
Suggestion 10

def main():
    #入力
    N = int(input())

    #初期化
    count = 0
    z = 2

    #処理
    while True:
        if N == 1:
            break
        elif N % z == 0:
            N = N // z
            count += 1
        else:
            z += 1

    #出力
    print(count)
