Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    if s.count('1') % 2 == 0:
        print('0')
    else:
        print('1')

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    if s.find('1') % 2 == 0:
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    if S[0] == '1':
        print("高桥")
    else:
        print("青木")

=======
Suggestion 4

def main():
    n = int(input())
    cards = input()
    print("Takahashi" if cards.index('1') % 2 == 0 else "Aoki")

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    if s.count('1') % 2 == 0:
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 6

def main():
    # 读入数据
    n = int(input())
    s = input()
    # 数据处理
    # 从前往后遍历，找到第一个1的位置
    for i in range(n):
        if s[i] == '1':
            # 判断是奇数还是偶数
            if i % 2 == 0:
                print('Takahashi')
            else:
                print('Aoki')
            break

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    if s.count('1') % 2:
        print('高桥')
    else:
        print('青木')

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    if s[0] == '0':
        print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 9

def main():
    N=int(input())
    S=input()
    if S.find('1')%2==0:
        print('Takahashi')
    else:
        print('Aoki')
