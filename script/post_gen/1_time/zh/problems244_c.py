Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(n):
    return 1

=======
Suggestion 2

def solve(n):
    a = 1
    b = 2*n+1
    while True:
        print(a)
        x = int(input())
        if x == 0:
            break
        if x < a:
            a = x
        elif x > b:
            b = x
        else:
            if a == x-1:
                a = x
            else:
                b = x

=======
Suggestion 3

def get_input():
    return int(input())

=======
Suggestion 4

def judge(n):
    if n < 0:
        return 1
    else:
        return 0

=======
Suggestion 5

def main():
    N = int(input())
    # 1 <= N <= 1000
    # 1 <= N <= 1000
    # N is an integer.
    # N是一个整数。
    print(1)
    # 高桥宣布一个整数1。
    # Takahashi announces an integer 1.
    # 高桥宣布一个整数1。
    # 高橋君は整数1を宣言する。
    print(int(input()) + 1)
    # 青木声明一个整数3。
    # Aoki declares an integer 3.
    # 青木宣布一个整数3。
    # 青木君は整数3を宣言する。
    # 高桥宣布一个整数2。
    # Takahashi announces an integer 2.
    # 高桥宣布一个整数2。
    # 高橋君は整数2を宣言する。
    print(int(input()) + 1)
    # 青木声明一个整数4。
    # Aoki declares an integer 4.
    # 青木宣布一个整数4。
    # 青木君は整数4を宣言する。
    # 高桥宣称有一个整数5。
    # Takahashi announces an integer 5.
    # 高桥宣称有一个整数5。
    # 高橋君は整数5を宣言する。
    print(int(input()) + 1)
    # 青木没有更多的整数可以申报，所以高桥赢了，游戏结束。
    # Aoki has no more integers to declare, so Takahashi wins and the game ends.
    # 青木没有更多的整数可以申报，所以高桥赢了，游戏结束。
    # 青木君はもう整数を宣言できないので、高橋君の勝ちでゲーム終了。
    # 青木君はもう整数

=======
Suggestion 6

def main():
    n = int(input())
    if n == 1:
        print(1)
        print(3)
        print(2)
        print(4)
    elif n == 2:
        print(3)
        print(1)
        print(4)
        print(2)
        print(5)
    elif n == 3:
        print(3)
        print(1)
        print(5)
        print(2)
        print(4)
        print(6)
    elif n == 4:
        print(5)
        print(1)
        print(3)
        print(6)
        print(2)
        print(4)
        print(7)
    elif n == 5:
        print(3)
        print(1)
        print(7)
        print(5)
        print(2)
        print(4)
        print(6)
        print(8)
    elif n == 6:
        print(5)
        print(1)
        print(3)
        print(7)
        print(2)
        print(6)
        print(4)
        print(8)
        print(9)
    elif n == 7:
        print(3)
        print(1)
        print(7)
        print(5)
        print(2)
        print(4)
        print(8)
        print(6)
        print(10)
    elif n == 8:
        print(5)
        print(1)
        print(3)
        print(7)
        print(2)
        print(4)
        print(8)
        print(6)
        print(10)
        print(9)
    elif n == 9:
        print(3)
        print(1)
        print(7)
        print(5)
        print(2)
        print(4)
        print(8)
        print(6)
        print(10)
        print(9)
        print(11)
    elif n == 10:
        print(5)
        print(1)
        print(3)
        print(7)
        print(2)
        print(6)
        print(4)
        print(8)
        print(10)
        print(9)
        print(11)
        print(12)
    elif n == 11:
        print(3)
        print(1)

=======
Suggestion 7

def main():
    n = int(input())
    print(1)
    i = int(input())
    if i == 2:
        print(3)
    else:
        print(2)
    while True:
        i = int(input())
        if i == 0:
            break
        print(i+1)
        i = int(input())
        if i == 2:
            print(3)
        else:
            print(2)
    return

main()

=======
Suggestion 8

def main():
    N = int(input())
    if N == 1:
        print(1)
        print(2)
        print(0)
        exit()
    print(1)
    print(2)
    while True:
        a = int(input())
        if a == 0:
            exit()
        if a % 2 == 0:
            print(a+1)
        else:
            print(a-1)
main()
#解法2
# 1 2 3 4 5 6 7 8 9 10 11 12
# 1 2 4 3 6 5 8 7 10 9 12 11
# 1 2 4 3 6 5 8 7 10 9 12 11 14 13 16 15 18 17 20 19 22 21 24 23 26 25 28 27 30 29 32 31 34 33 36 35 38 37 40 39 42 41 44 43 46 45 48 47 50 49 52 51 54 53 56 55 58 57 60 59 62 61 64 63 66 65 68 67 70 69 72 71 74 73 76 75 78 77 80 79 82 81 84 83 86 85 88 87 90 89 92 91 94 93 96 95 98 97 100 99 102 101 104 103 106 105 108 107 110 109 112 111 114 113 116 115 118 117 120 119 122 121 124 123 126 125 128 127 130 129 132 131 134 133 136 135 138 137 140 139 142 141 144 143 146 145 148 147 150 149 152 151 154 153 156 155 158 157 160 159 162 161 164 163 166 165 168 167 170 169 172 171 174 173 176 175
