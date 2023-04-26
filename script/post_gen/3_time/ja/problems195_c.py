Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))):
        ans += i * (10 ** i - 10 ** (i - 1))
    ans += len(str(N)) * (N - (10 ** (len(str(N)) - 1)) + 1)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))):
        ans += i * (10 ** i - 10 ** (i-1))
    ans += len(str(N)) * (N - 10 ** (len(str(N)) - 1) + 1)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    cnt = 0
    for i in range(1, len(str(N))+1):
        if N >= 10**(3*i):
            cnt += (N - 10**(3*i) + 1) * i
    print(cnt)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))):
        ans += (N // (10 ** (3 * i))) * (3 * i)
    ans += (N % (10 ** 3))
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1,15):
        ans += (N - 10**i + 1) * i
        N = 10**i - 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1, 17):
        ans += (N // (10 ** (3 * i))) * (i - 1) * (10 ** (3 * (i - 1)))
        ans += max(0, N - (10 ** (3 * i) - 1)) // (10 ** (3 * (i - 1)))
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    if N <= 999:
        print(0)
        return
    N = N - 999
    ans = 0
    i = 0
    while N > 0:
        ans += N % 1000
        N = N // 1000
        i += 1
        ans += i * 1
    ans -= 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))+1):
        ans += (N//(10**(3*i)))*3
    print(ans)

=======
Suggestion 9

def main():
    n = input()
    n = int(n)
    ans = 0
    for i in range(1,len(str(n))):
        ans += i * (n // (10 ** i) - n // (10 ** (i + 1)) * 10)
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    # 1000 ごとにコンマが入るので、1000 で割った商がコンマの数になる
    print((len(str(N)) - 1) // 3)
