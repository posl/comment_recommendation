Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 5 つの変数 x_1, x_2, x_3, x_4, x_5 があります。
    # 最初、変数 x_i には整数 i が代入されていました。
    # すぬけくんは、これらの変数の中から 1 つを選んで、その変数に 0 を代入する操作を行いました。
    # すぬけくんがこの操作を行ったあとの 5 つの変数の値が与えられます。
    # すぬけくんが 0 を代入した変数がどれであったかを答えてください。
    # 入力
    # 入力は以下の形式で標準入力から与えられる。
    # x_1 x_2 x_3 x_4 x_5
    # 出力
    # すぬけくんが 0 を代入した変数が x_i であるとき、整数 i を出力せよ。
    # 入力例 1
    # 0 2 3 4 5
    # 出力例 1
    # 1
    # この場合、すぬけくんが 0 を代入した変数は x_1 なので、1 を出力します。
    # 入力例 2
    # 1 2 0 4 5
    # 出力例 2
    # 3
    x = [int(x) for x in input().split()]
    print(x.index(0) + 1)

=======
Suggestion 2

def main():
    x = list(map(int, input().split()))
    for i in range(5):
        if x[i] == 0:
            print(i+1)
            break

=======
Suggestion 3

def main():
    x = list(map(int, input().split()))
    for i in range(5):
        if x[i] == 0:
            print(i+1)
            break

main()

=======
Suggestion 4

def main():
    x = list(map(int, input().split()))
    print(x.index(0) + 1)

=======
Suggestion 5

def main():
    x1,x2,x3,x4,x5 = map(int, input().split())
    print(x1.index(0)+1)

=======
Suggestion 6

def main():
    # 入力
    x = input().split()
    # 出力
    print(x.index('0') + 1)
