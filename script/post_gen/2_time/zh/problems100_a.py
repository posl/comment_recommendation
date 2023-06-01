Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读取输入
    A, B = map(int, input().split())

    # 判断是否满足条件
    if A <= 8 and B <= 8:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 2

def main():
    a,b=map(int,input().split())
    if a<=8 and b<=8:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 3

def main():
    a,b = map(int, input().split())
    if a > 8 or b > 8:
        print(":(")
    else:
        print("Yay!")

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a <= 8 and b <= 8:
        print('Yay!')
    else:
        print(':(')

=======
Suggestion 5

def get_input():
    input_str = input()
    input_str_list = input_str.split(" ")
    return {"A":int(input_str_list[0]),"B":int(input_str_list[1])}

=======
Suggestion 6

def main():
    A,B = map(int,input().split())
    if (A<=8 and B<=8):
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 7

def main():
    A,B = map(int,input().split())
    if A <= 8 and B <= 8:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 8

def solve():
    A,B = map(int,input().split())
    if A>8 or B>8:
        print(':(')
    else:
        print('Yay!')
