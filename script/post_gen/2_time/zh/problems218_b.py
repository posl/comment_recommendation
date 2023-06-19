Synthesizing 10/10 solutions

=======
Suggestion 1

def get_char(num):
    return chr(ord('a') + num - 1)

=======
Suggestion 2

def main():
    p=list(map(int,input().split()))
    a=[chr(96+i) for i in p]
    print(''.join(a))

=======
Suggestion 3

def main():
    p = list(map(int, input().split()))
    p = [chr(ord('a') + x - 1) for x in p]
    print(''.join(p))

=======
Suggestion 4

def main():
    str = input()
    num = str.split(' ')
    for i in range(26):
        print(chr(int(num[i])+96), end='')

=======
Suggestion 5

def main():
    p = list(map(int,input().split()))
    s = []
    for i in range(26):
        s.append(chr(p[i]+96))
    print("".join(s))

=======
Suggestion 6

def main():
    p = list(map(int, input().split()))
    s = []
    for i in range(26):
        s.append(chr(p[i]+96))
    print(''.join(s))

=======
Suggestion 7

def main():
    p = list(map(int, input().split()))
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    ans = ''
    for i in p:
        ans += alpha[i-1]
    print(ans)

=======
Suggestion 8

def main():
    p = list(map(int, input().split()))
    s = [None] * 26
    for i in range(26):
        s[i] = chr(ord('a') + p[i] - 1)
    print("".join(s))

=======
Suggestion 9

def main():
    p = list(map(int, input().split()))
    s = []
    for i in p:
        s.append(chr(ord('a') + i - 1))
    print(''.join(s))

=======
Suggestion 10

def main():
    # 读取输入
    input_line = input()
    # 用空格分隔输入
    input_line = input_line.split(" ")
    # 创建一个长度为26的列表
    output_list = [0 for i in range(26)]
    # 用循环把输入的数字转换为字母
    for i in range(26):
        output_list[int(input_line[i]) - 1] = chr(i + 97)
    # 把列表转换为字符串
    output_str = "".join(output_list)
    # 输出结果
    print(output_str)
