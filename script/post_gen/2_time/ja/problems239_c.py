Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x1, y1, x2, y2 = map(int, input().split())
    dx = x2 - x1
    dy = y2 - y1
    x3 = x2 - dy
    y3 = y2 + dx
    x4 = x3 - dx
    y4 = y3 - dy
    print("Yes" if x3 == x4 and y3 == y4 else "No")

=======
Suggestion 2

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 + y1 + x2 + y2) % 2 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2 - x1
    y3 = y2 - y1
    x4 = -y3
    y4 = x3
    x5 = x4 + x1
    y5 = y4 + y1
    print("Yes" if (x5, y5) != (x2, y2) else "No")

=======
Suggestion 6

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x = x2 - x1
    y = y2 - y1
    if x == y or x == -y:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    x1, y1, x2, y2 = map(int, input().split())
    if abs(x1 - x2) == abs(y1 - y2):
        print("Yes")
    elif abs(x1 - x2) % 2 == 0 and abs(y1 - y2) % 2 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    x1, y1, x2, y2 = map(int, input().split())
    #print(x1, y1, x2, y2)
    if x1 == x2:
        print("Yes")
        return
    if y1 == y2:
        print("Yes")
        return
    if x1 + y1 == x2 + y2:
        print("Yes")
        return
    if x1 - y1 == x2 - y2:
        print("Yes")
        return
    print("No")

main()

=======
Suggestion 9

def main():
    # 入力
    x1, y1, x2, y2 = map(int, input().split())
    # 処理
    # x1, y1, x2, y2の差が等しい時
    if x1 - x2 == y1 - y2:
        ans = "Yes"
    # x1, y1, x2, y2の和が等しい時
    elif x1 + y1 == x2 + y2:
        ans = "Yes"
    else:
        ans = "No"
    # 出力
    print(ans)
