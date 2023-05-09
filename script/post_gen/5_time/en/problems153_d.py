Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def attack(h):
    if h == 1:
        return 1
    else:
        return 2 * attack(h // 2) + 1

H = int(input())
print(attack(H))

=======
Suggestion 2

def main():
    H = int(input())
    count = 1
    while H > 1:
        H = H // 2
        count = count * 2
    print(count * 2 - 1)

=======
Suggestion 3

def main():
    h = int(input())
    cnt = 0
    while h > 0:
        cnt += 1
        h = h // 2
    print(2**cnt-1)

=======
Suggestion 4

def solve():
    h = int(input())
    x = 1
    while True:
        if h == 1:
            return x
        else:
            x = x * 2
            h = h // 2

print(solve())

=======
Suggestion 5

def main():
    h = int(input())
    print(2**(h.bit_length())-1)

=======
Suggestion 6

def main():
    H = int(input())
    print(2**(H.bit_length())-1)

=======
Suggestion 7

def problems153_d(H):
    return 0

=======
Suggestion 8

def get_int(): return int(input())
