Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def dice_sum(a, b, c):
    if a >= 1 and a <= 6 and b >= 1 and b <= 6 and c >= 1 and c <= 6:
        print(7 - a + 7 - b + 7 - c)
    else:
        print("输入的数值不在范围内")

dice_sum(1, 4, 3)
dice_sum(5, 6, 4)
dice_sum(7, 8, 9)

=======
Suggestion 2

def main():
    # 读取输入
    a, b, c = map(int, input().split())

    # 计算答案
    ans = 7 - a + 7 - b + 7 - c

    # 打印答案
    print(ans)

=======
Suggestion 3

def sum_of_three_dice():
    a, b, c = map(int, input().split())
    print(21 - a - b - c)

=======
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    print(21-a-b-c)
    
main()

=======
Suggestion 5

def main():
    a,b,c = map(int, input().split())
    print(7-a+7-b+7-c)

=======
Suggestion 6

def main():
    a,b,c = map(int,input().split())
    print(7-a+7-b+7-c)
main()

=======
Suggestion 7

def dice_sum(a,b,c):
    return 21-a-b-c

a,b,c = map(int,input().split())
print(dice_sum(a,b,c))

=======
Suggestion 8

def main():
    a,b,c = map(int, input().split())
    print(21-a-b-c)

=======
Suggestion 9

def dice(a,b,c):
    return 21-a-b-c

print(dice(1,4,3))
print(dice(5,6,4))
