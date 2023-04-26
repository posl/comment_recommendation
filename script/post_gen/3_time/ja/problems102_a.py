Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N % 2 == 0:
        print(N)
    else:
        print(N * 2)

=======
Suggestion 2

def main():
    N = int(input())
    i = 1
    while True:
        if (i % 2 == 0) or (i % N == 0):
            print(i)
            break
        i += 1

=======
Suggestion 3

def main():
    # 入力
    N = int(input())
    # 処理
    if N % 2 == 0:
        print(N)
    else:
        print(N * 2)

=======
Suggestion 4

def main():
    N = int(input())
    print(N * 2)

=======
Suggestion 5

def main():
    N = int(input())
    print(2 * N)

=======
Suggestion 6

def main():
    n = int(input())
    print(n*2)

=======
Suggestion 7

def main():
    N = int(input())
    print(lcm(N, 2))
