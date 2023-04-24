Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if len(str(i)) % 2 == 1:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    #入力
    N = int(input())
    #処理
    ans = 0
    for i in range(1,N+1):
        if len(str(i)) % 2 == 1:
            ans += 1
    #出力
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    if n < 10:
        print(n)
    else:
        print(9 + (n - 9) // 2)

=======
Suggestion 4

def main():
    N = int(input())
    print((N+1)//2)

=======
Suggestion 5

def main():
    N = int(input())
    print(N//2)

=======
Suggestion 6

def main():
    N = int(input())
    print(N - (N // 2) - (N // 10**5))

=======
Suggestion 7

def main():
    N = int(input())
    print(N//2 + N%2)
