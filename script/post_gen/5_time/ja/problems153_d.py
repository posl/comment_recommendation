Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def count_attack(h):
    if h == 1:
        return 1
    else:
        return 2 * count_attack(h // 2) + 1

h = int(input())
print(count_attack(h))

=======
Suggestion 2

def main():
    H = int(input())
    count = 0
    while H >= 1:
        count += 1
        H = H // 2
    print(2**count - 1)

=======
Suggestion 3

def f(x):
    if x == 1:
        return 1
    else:
        return 2 * f(x//2) + 1

H = int(input())
print(f(H))

=======
Suggestion 4

def main():
    h = int(input())
    cnt = 0
    while h > 0:
        cnt += 1
        h //= 2
    print(2 ** cnt - 1)

=======
Suggestion 5

def solve():
    H = int(input())
    ans = 0
    while H > 0:
        ans += H
        H //= 2
    print(ans)

=======
Suggestion 6

def main():
    H = int(input())
    count = 0
    while H > 0:
        H = H // 2
        count += 1
    print(2 ** count - 1)

=======
Suggestion 7

def main():
    H = int(input())
    cnt = 0
    while H > 0:
        cnt += 1
        H = H // 2
    print(2**cnt-1)

=======
Suggestion 8

def main():
    h = int(input())
    print(2**(h.bit_length())-1)

=======
Suggestion 9

def main():
    H = int(input())
    print(int((H**0.5)//1)*2-1)
    return
