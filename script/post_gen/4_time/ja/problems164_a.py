Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s, w = map(int, input().split())
    if w >= s:
        print("unsafe")
    else:
        print("safe")

=======
Suggestion 2

def main():
    s, w = map(int, input().split())
    if s <= w:
        print("unsafe")
    else:
        print("safe")

=======
Suggestion 3

def main():
    S, W = map(int, input().split())
    if S <= W:
        print("unsafe")
    else:
        print("safe")

=======
Suggestion 4

def solve():
    s, w = map(int, input().split())
    if s <= w:
        print("unsafe")
    else:
        print("safe")

=======
Suggestion 5

def main():
    s, w = map(int, input().split())
    print("unsafe" if s <= w else "safe")

=======
Suggestion 6

def solve():
    S, W = map(int, input().split())
    print("safe" if S > W else "unsafe")
