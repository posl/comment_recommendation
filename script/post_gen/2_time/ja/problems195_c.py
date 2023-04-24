Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = input()
    N = N[::-1]
    ans = 0
    for i in range(len(N)):
        if i % 3 == 2 and i != len(N)-1:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1,16):
        ans += (N//(10**i)-N//(10**(i+1)))*i
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(len(str(N))):
        if i == 0:
            continue
        ans += (N - 10**i + 1) * i
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    cnt = 0
    for i in range(1, len(str(N))+1):
        if i % 3 == 0:
            cnt += (N // (10**i)) * (10**(i-1)) + (N % (10**i) - (10**(i-1) - 1))
        else:
            cnt += (N // (10**i)) * (10**(i-1))
    print(cnt)

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))+1):
        ans += (N // (10**i)) * i
        ans += max(0, (N % (10**i) - 10**(i-1) + 1))
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))+1):
        ans += (N//(10**i))*i
        if N % (10**i) >= 10**(i-1):
            ans += N % (10**i) - 10**(i-1) + 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    if N < 1000:
        print(0)
    else:
        N = N - 999
        N = N // 1000
        print(N * (N + 1) // 2 + N)

=======
Suggestion 8

def main():
    N = int(input())
    #N = 27182818284590
    #N = 1010
    #N = 1000
    #N = 999
    #N = 100
    #N = 99
    #N = 10
    #N = 9
    #N = 1
    #N = 0
    #N = 1234567
    #N = 777
    #N = 1000000000000000
    #N = 10000000000000000
    #N = 100000000000000000
    #N = 1000000000000000000
    #N = 10000000000000000000
    #N = 100000000000000000000
    #N = 1000000000000000000000
    #N = 10000000000000000000000
    #N = 100000000000000000000000
    #N = 1000000000000000000000000
    #N = 10000000000000000000000000
    #N = 100000000000000000000000000
    #N = 1000000000000000000000000000
    #N = 10000000000000000000000000000
    #N = 100000000000000000000000000000
    #N = 1000000000000000000000000000000
    #N = 10000000000000000000000000000000

    #整数を書くとき、下から 3 桁ごとにコンマで区切って書きます。例えば 1234567 であれば 1,234,567、777 であれば 777 と書きます。
    #高橋君が 1 以上 N 以下の整数を 1 度ずつ書くとき、コンマは合計で何回書かれますか？
    print(N+1-(10**0+10**3+10**6+10**9+10**12+10**15))

=======
Suggestion 9

def main():
    n = int(input())
    a = 0
    while n >= 1000:
        n = n // 1000
        a += 1
    print(a)

=======
Suggestion 10

def comma_count(n):
    # n以下の整数を1度ずつ書くとき、コンマは合計で何回書かれるか
    if n < 1000:
        return 0
    else:
        return n//1000 + comma_count(n//1000)

n = int(input())
print(comma_count(n))
