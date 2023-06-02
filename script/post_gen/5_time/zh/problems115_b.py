Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    prices = []
    for i in range(N):
        prices.append(int(input()))
    max_price = max(prices)
    total = sum(prices)
    total -= max_price / 2
    print(int(total))

=======
Suggestion 2

def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    p[n-1] = p[n-1] // 2
    print(sum(p))

=======
Suggestion 3

def solve():
    n = int(input())
    plist = []
    for i in range(n):
        plist.append(int(input()))
    plist.sort()
    plist.reverse()
    plist[0] = plist[0] / 2
    print(int(sum(plist)))

=======
Suggestion 4

def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    p.reverse()
    p[0] = p[0] / 2
    print(int(sum(p)))

=======
Suggestion 5

def get_input():
    #输入
    N = int(input())
    p = [0] * N
    for i in range(N):
        p[i] = int(input())
    return N, p

=======
Suggestion 6

def main():
    n = int(input())
    p_list = []
    for i in range(n):
        p_list.append(int(input()))
    p_list.sort(reverse=True)
    p_list[0] = p_list[0] / 2
    print(int(sum(p_list)))

=======
Suggestion 7

def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort(reverse=True)
    p[0] = p[0] / 2
    print(int(sum(p)))

=======
Suggestion 8

def get_input():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    return n, p

=======
Suggestion 9

def main():
    n = int(input())
    prices = [int(input()) for i in range(n)]
    prices.sort(reverse=True)
    prices[0] = prices[0] // 2
    print(sum(prices))

=======
Suggestion 10

def problem115_b():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    p.reverse()
    p[0] /= 2
    print(int(sum(p)))
