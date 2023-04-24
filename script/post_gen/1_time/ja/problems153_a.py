Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, A = map(int, input().split())
    print((H + A - 1) // A)

=======
Suggestion 2

def main():
    h, a = map(int, input().split())
    print((h + a - 1) // a)

=======
Suggestion 3

def main():
    H, A = map(int, input().split())
    print(H//A if H%A == 0 else H//A + 1)

=======
Suggestion 4

def main():
    H, A = map(int, input().split())
    print(H // A + (1 if H % A else 0))

=======
Suggestion 5

def main():
    #入力
    H, A = map(int, input().split())

    #出力
    print((H + A - 1) // A)
