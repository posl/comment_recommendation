Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S, W = map(int, input().split())
    if S <= W:
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
    sheep, wolf = map(int, input().split())
    if wolf >= sheep:
        print("unsafe")
    else:
        print("safe")

=======
Suggestion 4

def main():
    S, W = map(int, input().split())

    if S > W:
        print("safe")
    else:
        print("unsafe")

=======
Suggestion 5

def main():
    s,w = map(int, input().split())
    if w >= s:
        print('unsafe')
    else:
        print('safe')

=======
Suggestion 6

def main():
    S, W = map(int, input().split())
    if W >= S:
        print("unsafe")
    else:
        print("safe")
main()

=======
Suggestion 7

def main():
    S,W = map(int,input().split())
    if W >= S:
        print("unsafe")
    else:
        print("safe")

=======
Suggestion 8

def main():
    s,w = map(int, input().split())
    if s > w:
        print('safe')
    else:
        print('unsafe')

=======
Suggestion 9

def main():
    s, w = map(int, input().split())
    print("safe" if s > w else "unsafe")

=======
Suggestion 10

def unsafe(s,w):
    if w >= s:
        print("unsafe")
    else:
        print("safe")
