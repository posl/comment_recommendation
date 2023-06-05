Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem164_a(s,w):
    if w>=s:
        print('不安全')
    else:
        print('安全')

problem164_a(4,5)
problem164_a(100,2)
problem164_a(10,10)

=======
Suggestion 2

def main():
    s, w = map(int, input().split())
    if s > w:
        print('安全')
    else:
        print('不安全')

=======
Suggestion 3

def main():
    s, w = map(int, input().split())
    print("安全" if s > w else "不安全")

=======
Suggestion 4

def main():
    s, w = map(int, input().split())
    if s <= w:
        print("unsafe")
    else:
        print("safe")

=======
Suggestion 5

def main():
    s,w = map(int,input().split())
    if w >= s:
        print("不安全")
    else:
        print("安全")

=======
Suggestion 6

def main():
    s, w = map(int, input().split())
    if w >= s:
        print('unsafe')
    else:
        print('safe')

=======
Suggestion 7

def main():
    sheep, wolf = map(int, input().split())
    if sheep <= wolf:
        print("不安全")
    else:
        print("安全")

=======
Suggestion 8

def main():
    s,w = map(int, input().split())
    if s <= w:
        print("不安全")
    else:
        print("安全")
