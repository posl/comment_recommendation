Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    c = input()
    print(chr(ord(c) + 1))

=======
Suggestion 2

def main():
    c = input("请输入一个小写英文字母：")
    if c == 'z':
        print("输入的字母是z，没有后面的字母")
    else:
        print("输入的字母是%s，它后面的字母是%s"%(c,chr(ord(c)+1)))

=======
Suggestion 3

def main():
    c = input()
    if c == 'z':
        print('z')
    else:
        print(chr(ord(c) + 1))

=======
Suggestion 4

def main():
    c = input()
    print(chr(ord(c) + 1))
main()

=======
Suggestion 5

def solution(c):
    print(chr(ord(c)+1))

=======
Suggestion 6

def solve(input):
    return chr(ord(input)+1)
