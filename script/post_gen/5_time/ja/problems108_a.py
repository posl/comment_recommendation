Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    K = int(input())
    print((K // 2) * (K // 2 + K % 2))

=======
Suggestion 2

def main():
    K = int(input())
    if K % 2 == 0:
        print((K // 2) ** 2)
    else:
        print((K // 2) * (K // 2 + 1))

=======
Suggestion 3

def main():
    k = int(input())
    if k % 2 == 0:
        print(int((k/2))**2)
    else:
        print(int((k/2)) * (int((k/2))+1))

=======
Suggestion 4

def calc(k):
    # 偶数の個数
    even = k // 2
    # 奇数の個数
    odd = k - even
    return even * odd

=======
Suggestion 5

def main():
    k = int(input())
    if k % 2 == 0:
        print(int((k / 2) ** 2))
    else:
        print(int(((k - 1) / 2) * ((k + 1) / 2)))

=======
Suggestion 6

def main():
    k = int(input())
    if k % 2 == 0:
        print(int((k/2)**2))
    else:
        print(int((k/2)*(k/2+1)))

=======
Suggestion 7

def main():
    K = int(input())
    if K % 2 == 0:
        print(int((K/2)**2))
    else:
        print(int((K//2)*(K//2 + 1)))

=======
Suggestion 8

def solve():
    k = int(input())
    if k % 2 == 0:
        print(int(k/2)**2)
    else:
        print(int((k+1)/2)*int((k-1)/2))

=======
Suggestion 9

def calc_even_odd_pairs(n):
    if n % 2 == 0:
        return int(n/2) * int(n/2)
    else:
        return int(n/2) * (int(n/2) + 1)

=======
Suggestion 10

def main():
    k = int(input())
    if k % 2 == 0:
        print(int((k/2)**2))
    else:
        print(int((k//2)*(k//2+1)))
