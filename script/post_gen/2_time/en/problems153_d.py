Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H = int(input())
    count = 0
    while H > 0:
        H = H // 2
        count += 1
    print(2 ** count - 1)

=======
Suggestion 2

def main():
    H = int(input())
    ans = 0
    while H > 0:
        ans += H
        H //= 2
    print(ans)

=======
Suggestion 3

def main():
    h = int(input())
    ans = 0
    while h > 0:
        ans += h
        h //= 2
    print(ans)

=======
Suggestion 4

def main():
    h = int(input())
    ans = 0
    while h > 0:
        h = h // 2
        ans += 1
    print(2 ** ans - 1)

=======
Suggestion 5

def main():
    H = int(input())
    ans = 0
    while H > 0:
        ans += 2 ** (H.bit_length() - 1)
        H -= 2 ** (H.bit_length() - 1)
    print(ans)

=======
Suggestion 6

def main():
    H = int(input())
    if H == 1:
        print(1)
    else:
        print(2**H.bit_length() - 1)

=======
Suggestion 7

def main():
    H = int(input())
    print(2**H.bit_length()-1)

=======
Suggestion 8

def get_input():
    return int(input())
