Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S, W = map(int, input().split())
    if W >= S:
        print('unsafe')
    else:
        print('safe')

main()

=======
Suggestion 2

def main():
    s, w = map(int, input().split())
    if w >= s:
        print("unsafe")
    else:
        print("safe")

=======
Suggestion 3

def main():
    S, W = map(int, input().split())
    if S <= W:
        print('unsafe')
    else:
        print('safe')

=======
Suggestion 4

def main():
    s, w = map(int, input().split())
    if s > w:
        print('safe')
    else:
        print('unsafe')

=======
Suggestion 5

def main():
    S, W = map(int, input().split())
    if S > W:
        print('safe')
    else:
        print('unsafe')

=======
Suggestion 6

def main():
    sheep, wolves = map(int, input().split())
    if wolves >= sheep:
        print('unsafe')
    else:
        print('safe')

main()

=======
Suggestion 7

def main():
    s, w = map(int, input().split())
    if s > w:
        print("safe")
    else:
        print("unsafe")
main()

=======
Suggestion 8

def main():
    s,w = map(int,input().split())
    if w >= s:
        print('unsafe')
    else:
        print('safe')

=======
Suggestion 9

def main():
    s,w = map(int, input().split())
    if s <= w:
        print("unsafe")
    else:
        print("safe")

=======
Suggestion 10

def main():
    s, w = map(int, input().split())
    print('unsafe' if w >= s else 'safe')
