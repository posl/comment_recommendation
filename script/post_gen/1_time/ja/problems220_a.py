Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C = map(int, input().split())
    ans = -1
    for i in range(A, B + 1):
        if i % C == 0:
            ans = i
            break
    print(ans)

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    for i in range(A, B + 1):
        if i % C == 0:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            return
    print(-1)

=======
Suggestion 5

def main():
    A, B, C = map(int, input().split())
    for n in range(A, B+1):
        if n % C == 0:
            print(n)
            return
    print(-1)

=======
Suggestion 6

def main():
    #入力
    A, B, C = map(int, input().split())
    #出力
    for i in range(A, B+1):
        if i % C == 0:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 7

def main():
    # 入力
    A, B, C = map(int, input().split())
    # 処理
    for i in range(A, B+1):
        if i % C == 0:
            print(i)
            return

    print(-1)
    return

=======
Suggestion 8

def main():
    # A, B, C = map(int, input().split())
    # print(A, B, C)
    # for i in range(A, B + 1):
    #     if i % C == 0:
    #         print(i)
    #         break
    # else:
    #     print(-1)
    A, B, C = map(int, input().split())
    print(next(filter(lambda x: x % C == 0, range(A, B + 1)), -1))
