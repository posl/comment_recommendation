Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H = int(input())
    ans = 0
    while H > 0:
        H //= 2
        ans += 1
    print(2 ** ans - 1)

=======
Suggestion 2

def main():
    H = int(input())
    ans = 0
    while H > 0:
        H //= 2
        ans += 1
    print(2**ans-1)

main()

=======
Suggestion 3

def main():
    H = int(input())
    ans = 0
    while H > 0:
        ans += H
        H //= 2
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
        H = H // 2
        ans += 1
    print(2**ans-1)

=======
Suggestion 6

def main():
    h = int(input())
    k = 0
    while h > 0:
        h = h // 2
        k += 1
    print(2 ** k - 1)

main()

=======
Suggestion 7

def main():
    h = int(input())
    ans = 0
    while h > 0:
        ans += h
        h >>= 1
    print(ans)

=======
Suggestion 8

def main():
    H = int(input())
    ans = 0
    while H > 0:
        H //= 2
        ans = ans * 2 + 1
    print(ans)

=======
Suggestion 9

def main():
    H = int(input())
    print(2**H.bit_length() - 1)
