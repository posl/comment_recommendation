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

def main():
    s, w = map(int, input().split())
    if w >= s:
        print('unsafe')
    else:
        print('safe')

=======
Suggestion 5

def main():
    S, W = map(int, input().split())
    if S > W:
        print("safe")
    else:
        print("unsafe")

=======
Suggestion 6

def main():
    s,w = map(int,input().split())
    if s <= w:
        print('unsafe')
    else:
        print('safe')

=======
Suggestion 7

def check_safe(s,w):
    if s <= w:
        print("unsafe")
    else:
        print("safe")
