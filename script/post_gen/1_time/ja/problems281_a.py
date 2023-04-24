Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    for i in range(n, -1, -1):
        print(i)

=======
Suggestion 2

def main():
    N = int(input())
    for i in range(N,-1,-1):
        print(i)

=======
Suggestion 3

def main():
    N = int(input())
    for i in reversed(range(N+1)):
        print(i)

=======
Suggestion 4

def main():
    n = int(input())
    if n < 1 or n > 100:
        print('制約違反')
        return

    for i in range(n, -1, -1):
        print(i)
