Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort(reverse=True)
    sum = 0
    for i in range(N):
        if i == 0:
            sum += p[i] / 2
        else:
            sum += p[i]
    print(int(sum))

=======
Suggestion 2

def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]
    p.sort(reverse=True)
    ans = 0
    for i in range(N-1):
        ans += p[i]
    ans += p[N-1] / 2
    print(int(ans))

main()

=======
Suggestion 3

def main():
    N = int(input())
    prices = []
    for _ in range(N):
        prices.append(int(input()))
    prices.sort(reverse=True)
    ans = prices[0] / 2 + sum(prices[1:])
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort()
    p[-1] = p[-1] / 2
    print(int(sum(p)))

=======
Suggestion 5

def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))

    p.sort(reverse=True)
    p[0] = p[0] / 2

    print(int(sum(p)))

=======
Suggestion 6

def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]

    print(int(sum(p) - max(p) / 2))

=======
Suggestion 7

def main():
    # 入力
    N = int(input())
    p = [int(input()) for _ in range(N)]
    # 処理
    p.sort()
    p[-1] = p[-1] // 2
    # 出力
    print(sum(p))

=======
Suggestion 8

def main():
    N = int(input())
    p_list = []
    for i in range(N):
        p_list.append(int(input()))
    p_list.sort()
    p_list.reverse()
    ans = 0
    for i in range(N):
        if i == 0:
            ans += p_list[i] / 2
        else:
            ans += p_list[i]
    print(int(ans))

=======
Suggestion 9

def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort()
    print(sum(p[0:N-1]) + p[N-1]//2)

=======
Suggestion 10

def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]

    print(sum(p) - max(p)//2)
