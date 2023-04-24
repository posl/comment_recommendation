Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    print(7 - a + 7 - b + 7 - c)

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    print(21 - a - b - c)

=======
Suggestion 3

def main():
    # a, b, c = map(int, input().split())
    # print(7 - a + 7 - b + 7 - c)
    a, b, c = map(int, input().split())
    print(21 - a - b - c)

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    print(21 - (a + b + c))

=======
Suggestion 5

def main():
    # 標準入力から値を取得する
    a, b, c = map(int, input().split())
    print(21 - a - b - c)

=======
Suggestion 6

def main():
    #a, b, c = map(int, input().split())
    #print(21 - (a + b + c))
    print(21 - sum(map(int, input().split())))

=======
Suggestion 7

def dice(a,b,c):
    return 7 - a + 7 - b + 7 - c
