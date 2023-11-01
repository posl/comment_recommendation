Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(len(set(s)))

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())

=======
Suggestion 3

def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    print(len(s))

=======
Suggestion 4

def main():
    #读取输入
    n = int(input())
    s = [input() for i in range(n)]

    #去重
    s = list(set(s))

    #输出

=======
Suggestion 5

def main():
    n = int(input())
    s = [input() for i in range(n)]
    print(len(set(s)))

=======
Suggestion 6

def main():
    n = int(input())
    item = set()
    for i in range(n):
        item.add(input())
    print(len(item))

=======
Suggestion 7

def main():
    N = int(input())
    S = set()
    for i in range(N):
        S.add(input())
    print(len(S))
