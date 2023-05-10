Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int, input().split())
    if a > b:
        print(a - ((a - b) // 2))
    else:
        print(b - ((b - a) // 2))

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if (A + B) % 2 == 0:
        print((A + B) // 2)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 3

def main():
    # input
    A, B = map(int, input().split())

    # compute

    # output
    if (A+B)%2 == 0:
        print((A+B)//2)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    print((a + b) // 2 if (a + b) % 2 == 0 else 'IMPOSSIBLE')

=======
Suggestion 5

def main():
    # -*- coding: utf-8 -*-
    # 整数の入力
    a, b = map(int, input().split())
    # スペース区切りの整数の入力
    #a, b = map(int, input().split())
    # 文字列の入力
    #s = input()
    # 出力
    #print("{} {}".format(a+b+c, s))
    #print("{0} {1}".format(a+b+c, s))
    #print(f"{a+b+c} {s}")
    #print(f"{a+b+c=}, {s=}")
    #print(f"{a=}, {b=}")
    #print(f"{a=}")
    #print(f"{b=}")
    if (a - b) % 2 == 0:
        print((a + b) // 2)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    if (a + b) % 2 != 0:
        print('IMPOSSIBLE')
    else:
        print(int((a + b) / 2))

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    if a < b:
        print(b - (b - a) // 2)
    else:
        print(a - (a - b) // 2)

main()

=======
Suggestion 8

def main():
    a,b = map(int,input().split())
    if (a+b)%2 == 0:
        print((a+b)//2)
    else:
        print("IMPOSSIBLE")

=======
Suggestion 9

def main():
    a,b = map(int, input().split())
    k = (a+b)/2
    if k.is_integer():
        print(int(k))
    else:
        print("IMPOSSIBLE")
