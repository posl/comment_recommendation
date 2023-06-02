Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S, W = map(int, input().split())
    if W >= S:
        print('unsafe')
    else:
        print('safe')

=======
Suggestion 2

def is_safe(s, w):
    if s > w:
        return '安全'
    else:
        return '不安全'

=======
Suggestion 3

def main():
    S, W = map(int, input().split())
    if S > W:
        print("安全")
    else:
        print("不安全")

=======
Suggestion 4

def main():
    S, W = map(int, input().split())
    if S <= W:
        print("unsafe")
    else:
        print("safe")

=======
Suggestion 5

def main():
    s,w = map(int, input().split())
    if s <= w:
        print("不安全")
    else:
        print("安全")

=======
Suggestion 6

def main():
    S, W = map(int, input().split())
    if S <= W:
        print('unsafe')
    else:
        print('safe')

=======
Suggestion 7

def main():
    s,w = map(int,input().split())
    if s > w:
        print('安全')
    else:
        print('不安全')

=======
Suggestion 8

def main():
    S, W = map(int, input().split())
    if S > W:
        print('安全')
    else:
        print('不安全')
