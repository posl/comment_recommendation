Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]
    p.sort(reverse=True)
    ans = 0
    for i in range(N):
        if i == 0:
            ans += p[i] // 2
        else:
            ans += p[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    p_list = []
    for i in range(N):
        p_list.append(int(input()))
    p_list.sort()
    total = 0
    for i in range(N):
        if i == N-1:
            total += p_list[i]//2
        else:
            total += p_list[i]
    print(total)

=======
Suggestion 3

def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]
    p.sort()
    ans = sum(p[:-1]) + p[-1] // 2
    print(ans)

=======
Suggestion 4

def main():
    num = int(input())
    prices = []
    for i in range(num):
        prices.append(int(input()))
    prices.sort(reverse=True)
    total = 0
    for i in range(num):
        if i == 0:
            total += (prices[i] / 2)
        else:
            total += prices[i]
    print(int(total))

=======
Suggestion 5

def main():
    N = int(input())
    p_list = []
    for i in range(N):
        p_list.append(int(input()))
    p_list.sort(reverse = True)
    p_list[0] = int(p_list[0] / 2)
    print(sum(p_list))

=======
Suggestion 6

def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort()
    print(sum(p[:-1]) + p[-1]//2)

=======
Suggestion 7

def main():
    N = int(input())
    P = [int(input()) for i in range(N)]
    P.sort(reverse = True)
    for i in range(N):
        if i == 0:
            total = P[i] / 2
        else:
            total += P[i]
    print(int(total))

=======
Suggestion 8

def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p = sorted(p, reverse=True)
    for i in range(1, N):
        p[0] = int(p[0] / 2)
    print(sum(p))

=======
Suggestion 9

def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort()
    #print(p)
    p[-1] = p[-1] / 2
    #print(p)
    print(int(sum(p)))

=======
Suggestion 10

def main():
    #入力
    N = int(input())
    p_list = []
    for i in range(N):
        p_list.append(int(input()))
    #ソート
    p_list.sort()
    #最大値を半額にする
    p_list[-1] = p_list[-1] / 2
    #合計
    ans = sum(p_list)
    #出力
    print(int(ans))

main()
