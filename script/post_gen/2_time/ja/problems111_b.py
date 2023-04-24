Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    if N % 111 == 0:
        print(N)
    else:
        print((N // 111 + 1) * 111)

=======
Suggestion 2

def main():
    n = int(input())
    if n % 111 == 0:
        print(n)
    else:
        print((n // 111 + 1) * 111)

=======
Suggestion 3

def main():
    N = input()
    if len(N) == 3:
        print(N)
    elif len(N) == 2:
        print("".join([N[0],N[0],N[0]]))
    elif len(N) == 1:
        print("".join([N, N, N]))

=======
Suggestion 4

def check(n):
    s = str(n)
    if s[0] == s[1] and s[1] == s[2]:
        return True
    return False

n = int(input())
while True:
    if check(n):
        print(n)
        exit()
    n += 1

=======
Suggestion 5

def main():
    N = int(input())
    while True:
        if N % 111 == 0:
            print(N)
            break
        N += 1

=======
Suggestion 6

def main():
    n = int(input())
    # 111, 222, 333, 444, 555, 666, 777, 888, 999
    # 111, 222, 333, 444, 555, 666, 777, 888, 999
    # 111, 222, 333, 444, 555, 666, 777, 888, 999
    # 111, 222, 333, 444, 555, 666, 777, 888, 999
    # 111, 222, 333, 444, 555, 666, 777, 888, 999
    # 111, 222, 333, 444, 555, 666, 777, 888, 999
    # 111, 222, 333, 444, 555, 666, 777, 888, 999
    # 111, 222, 333, 444, 555, 666, 777, 888, 999
    # 111, 222, 333, 444, 555, 666, 777, 888, 999
    if n % 111 == 0:
        print(n)
    else:
        print((n // 111 + 1) * 111)

=======
Suggestion 7

def main():
    n = int(input())
    print(((n-1)//111+1)*111)

=======
Suggestion 8

def main():
    N = int(input())
    # N = 111
    # N = 112
    # N = 750

    # 1桁目が1の場合
    if N % 111 == 0:
        print(N)
    # 1桁目が1以外の場合
    else:
        print((N // 111 + 1) * 111)
