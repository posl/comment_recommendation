Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        if len(str(i)) % 2 == 1:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if len(str(i)) % 2 == 1:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N + 1):
        if len(str(i)) % 2 == 1:
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    N = int(input())
    even = 0
    odd = 0
    for i in range(1,N+1):
        if len(str(i)) % 2 == 0:
            even += 1
        else:
            odd += 1
    print(odd)

=======
Suggestion 5

def main():
    N = int(input())

    if N < 10:
        print(N)
    else:
        print(9 + (N - 9) // 2)

=======
Suggestion 6

def main():
    N = int(input())

    # 1桁の数は9個
    # 2桁の数は90個
    # 3桁の数は900個
    # 4桁の数は9000個
    # 5桁の数は90000個
    # 6桁の数は900000個
    # 7桁の数は9000000個
    # 8桁の数は90000000個
    # 9桁の数は900000000個
    # 10桁の数は9000000000個
    # 11桁の数は90000000000個
    # 12桁の数は900000000000個
    # 13桁の数は9000000000000個
    # 14桁の数は90000000000000個
    # 15桁の数は900000000000000個
    # 16桁の数は9000000000000000個
    # 17桁の数は90000000000000000個
    # 18桁の数は900000000000000000個
    # 19桁の数は9000000000000000000個
    # 20桁の数は90000000000000000000個
    # 21桁の数は900000000000000000000個
    # 22桁の数は9000000000000000000000個
    # 23桁の数は90000000000000000000000個
    # 24桁の数は900000000000000000000000個
    # 25桁の数は9000000000000000000000000個
    # 26桁の数は90000000000000000000000000個
    # 27桁の数は900000000000000000000000000個
    # 28桁の数は9000000000000000000000000000個
    # 29桁の数は900000

=======
Suggestion 7

def main():
    n = int(input())
    print(n // 2 + n % 2)

=======
Suggestion 8

def main():
    N = int(input())
    print(N - N // 2)

=======
Suggestion 9

def main():
    n = int(input())
    print(n//2)

=======
Suggestion 10

def main():
    N = int(input())
    print(N//2 + N%2)
