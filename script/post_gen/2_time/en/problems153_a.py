Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, A = map(int, input().split())
    if H % A == 0:
        print(H // A)
    else:
        print(H // A + 1)

=======
Suggestion 2

def main():
    H, A = map(int, input().split())
    print((H + A - 1) // A)

=======
Suggestion 3

def main():
    h, a = map(int, input().split())
    print((h + a - 1) // a)

=======
Suggestion 4

def main():
    H, A = map(int, input().split())
    print((H - 1) // A + 1)

=======
Suggestion 5

def main():
    h, a = map(int, input().split())
    print(h // a + 1 if h % a else h // a)

=======
Suggestion 6

def main():
    h, a = map(int, input().split())
    print(h // a + (h % a > 0))
