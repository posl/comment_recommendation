Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S, W = map(int, input().split())
    if S > W:
        print("安全")
    else:
        print("不安全")

=======
Suggestion 2

def solve():
    S, W = map(int, input().split())
    if S <= W:
        print('unsafe')
    else:
        print('safe')

=======
Suggestion 3

def main():
    str = input()
    strlist = str.split()
    s = int(strlist[0])
    w = int(strlist[1])
    if s > w:
        print("安全")
    else:
        print("不安全")

=======
Suggestion 4

def main():
    S, W = map(int, input().split())
    if W >= S:
        print("unsafe")
    else:
        print("safe")

=======
Suggestion 5

def main():
    S,W=map(int,input().split())
    if S>W:
        print('安全')
    else:
        print('不安全')

=======
Suggestion 6

def main():
    S, W = map(int, input().split())
    if S <= W:
        print("unsafe")
    else:
        print("safe")

=======
Suggestion 7

def f(S,W):
    if S<=W:
        print('不安全')
    else:
        print('安全')

=======
Suggestion 8

def main():
    s,w = map(int,input().split())
    if s<=w:
        print('unsafe')
    else:
        print('safe')

=======
Suggestion 9

def main():
    S, W = map(int, input().split())
    if W >= S:
        print('unsafe')
    else:
        print('safe')
