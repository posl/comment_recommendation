Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if a + b + c >= 22:
        print("bust")
    else:
        print("win")

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if a + b + c >= 22:
        print('bust')
    else:
        print('win')

=======
Suggestion 3

def main():
    a = list(map(int, input().split()))
    if sum(a) >= 22:
        print("bust")
    else:
        print("win")
