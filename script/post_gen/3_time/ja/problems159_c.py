Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    L = int(input())
    if L % 3 == 0:
        print((L / 3) ** 3)
    else:
        print((L // 3 + 1) ** 3 * (L // 3) ** 3 * (L // 3) ** 3)

=======
Suggestion 2

def main():
    L = int(input())
    if L % 3 == 0:
        print((L/3)**3)
    else:
        print((L//3+1)**3)

=======
Suggestion 3

def main():
    L = int(input())

    if L % 3 == 0:
        print((L // 3) ** 3)
    else:
        print((L // 3) ** 3 * (L % 3))

=======
Suggestion 4

def main():
    # 入力
    L = int(input())

    # 処理
    ans = (L/3)**3

    # 出力
    print(ans)

=======
Suggestion 5

def main():
    L = int(input())
    print((L/3)**3)

main()

=======
Suggestion 6

def main():
    L = int(input())
    ans = (L/3)**3
    print(ans)

=======
Suggestion 7

def main():
    L = int(input())
    print((L/3)**3)

=======
Suggestion 8

def main():
    l = int(input())
    print((l/3)**3)
