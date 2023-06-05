Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort(reverse=True)
    price = sum(p)
    price -= p[0] / 2
    print(int(price))

=======
Suggestion 2

def main():
    n = int(input())
    p_list = []
    for i in range(n):
        p_list.append(int(input()))
    p_list.sort()
    p_list[-1] = p_list[-1] // 2
    print(sum(p_list))

=======
Suggestion 3

def main():
    n = int(input())
    p_list = [int(input()) for i in range(n)]
    p_list.sort(reverse=True)
    p_list[0] = p_list[0] // 2
    print(sum(p_list))
    return

=======
Suggestion 4

def main():
    n = int(input())
    p = [int(input()) for i in range(n)]
    p.sort()
    print(int(sum(p) - p[-1]/2))

=======
Suggestion 5

def main():
    n = int(input())
    price = []
    for i in range(n):
        price.append(int(input()))
    price.sort(reverse=True)
    price[0] = price[0] / 2
    print(int(sum(price)))

=======
Suggestion 6

def problem115_b():
    n = int(input())
    p = [int(input()) for i in range(n)]
    max = 0
    for i in range(n):
        if p[i] > max:
            max = p[i]
    total = 0
    for i in range(n):
        if p[i] == max:
            total += int(max / 2)
        else:
            total += p[i]
    print(total)

=======
Suggestion 7

def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort()
    p[-1] = int(p[-1] / 2)
    print(sum(p))

=======
Suggestion 8

def get_input():
    n = int(input())
    p_list = []
    for i in range(n):
        p_list.append(int(input()))
    return n, p_list

=======
Suggestion 9

def calc_price(n, price_list):
    price_list.sort()
    price_list[-1] = price_list[-1] / 2
    return sum(price_list)
