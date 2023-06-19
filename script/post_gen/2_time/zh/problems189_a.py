Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    input_str = input()
    if input_str[0] == input_str[1] == input_str[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 2

def main():
    C = input()
    if C[0] == C[1] and C[1] == C[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 3

def main():
  # 请在此添加您的代码
  c1,c2,c3 = input().split()
  if c1 == c2 and c2 == c3:
    print("Won")
  else:
    print("Lost")
  # 请在此添加您的代码

main()

=======
Suggestion 4

def main():
    c = input()
    if c[0] == c[1] == c[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 5

def main():
    c1, c2, c3 = input().split()
    if c1 == c2 == c3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 6

def main():
    s = [str(i) for i in input()]
    if s[0] == s[1] == s[2]:
        print('Won')
    else:
        print('Lost')

=======
Suggestion 7

def main():
    # 读取输入
    c1,c2,c3 = input().split()
    # 处理
    if c1 == c2 == c3:
        result = "Won"
    else:
        result = "Lost"
    # 输出结果
    print(result)

=======
Suggestion 8

def main():
    # 读入一行
    line = input()
    # 用空格分割
    line = line.split()
    # 取第一个元素
    c1 = line[0]
    # 取第二个元素
    c2 = line[1]
    # 取第三个元素
    c3 = line[2]
    # 如果这三个元素相同
    if c1 == c2 and c2 == c3:
        # 打印Won
        print("Won")
    # 否则
    else:
        # 打印Lost
        print("Lost")

=======
Suggestion 9

def main():
    #输入
    C_1, C_2, C_3 = input().split()
    #处理
    if C_1 == C_2 == C_3:
        result = "Won"
    else:
        result = "Lost"
    #输出
    print(result)

=======
Suggestion 10

def main():
    a = input()
    if a[0] == a[1] == a[2]:
        print("Won")
    else:
        print("Lost")
