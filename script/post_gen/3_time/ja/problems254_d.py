Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i*j <= N:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i*j <= n:
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        ans += N//i - i + 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1, int(N**0.5)+1):
        for j in range(i, N+1):
            if i*j <= N:
                ans += 1
            else:
                break
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    i = 1
    ans = 0
    while i * i <= N:
        ans += N // (i * i)
        i += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    c = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j <= n and (i * j) ** 0.5 % 1 == 0:
                c += 1
    print(c)

=======
Suggestion 7

def main():
    N = int(input())
    N = int(N**0.5)
    print(N*(N+1))

main()

=======
Suggestion 8

def main():
    N = int(input())

    # 平方数のリスト
    squares = []
    for i in range(1, int(N**0.5)+1):
        squares.append(i**2)

    # 組み合わせのリスト
    combination = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            combination.append(i*j)

    # 平方数のリストと組み合わせのリストの積を集合に変換し、要素数を出力
    print(len(set(squares) & set(combination)))

=======
Suggestion 9

def find_squares(n):
    return [i ** 2 for i in range(1, int(n ** 0.5) + 1)]
