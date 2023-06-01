Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == 'L':
                print('No')
                exit()
        else:
            if S[i] == 'R':
                print('No')
                exit()
    print('Yes')

=======
Suggestion 2

def solve():
    S = input()
    for i in range(len(S)):
        if i & 1 and S[i] in 'RL':
            print('No')
            return
        if not i & 1 and S[i] in 'UD':
            print('No')
            return
    print('Yes')
solve()

=======
Suggestion 3

def main():
    s = input()
    if s[::2] == s[::2].replace('L', '').replace('U', '').replace('D', '') and s[1::2] == s[1::2].replace('R', '').replace('U', '').replace('D', ''):
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 4

def main():
    S = input()
    odd = S[0::2]
    even = S[1::2]
    if odd.find('L') == -1 and odd.find('R') == -1 and even.find('U') == -1 and even.find('D') == -1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    S = input()
    if len(S) % 2 == 0:
        print("Yes" if S[0::2].count("L") == 0 and S[1::2].count("R") == 0 else "No")
    else:
        print("No")

=======
Suggestion 6

def main():
    s = input()
    for i in range(0, len(s)):
        if i % 2 == 0:
            if s[i] == 'L':
                print('No')
                return
        else:
            if s[i] == 'R':
                print('No')
                return
    print('Yes')

=======
Suggestion 7

def main():
    S = input()
    if len(S) % 2 == 0:
        for i in range(0, len(S), 2):
            if S[i] == "L":
                print("No")
                exit()
        for i in range(1, len(S), 2):
            if S[i] == "R":
                print("No")
                exit()
    else:
        for i in range(0, len(S), 2):
            if S[i] == "R":
                print("No")
                exit()
        for i in range(1, len(S), 2):
            if S[i] == "L":
                print("No")
                exit()
    print("Yes")

=======
Suggestion 8

def main():
    s = input()
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == 'L':
                print('No')
                exit()
        else:
            if s[i] == 'R':
                print('No')
                exit()
    print('Yes')

=======
Suggestion 9

def main():
    # 读入输入
    s = input()
    # 计算奇数位置的字符是否是R、U或D
    for i in range(0, len(s), 2):
        if s[i] not in ['R', 'U', 'D']:
            print('No')
            return
    # 计算偶数位置的字符是否是L、U或D
    for i in range(1, len(s), 2):
        if s[i] not in ['L', 'U', 'D']:
            print('No')
            return
    # 输出结果
    print('Yes')

=======
Suggestion 10

def main():
    s=input()
    flag=True
    for i in range(len(s)):
        if i%2==0:
            if s[i] not in ['R','U','D']:
                flag=False
                break
        else:
            if s[i] not in ['L','U','D']:
                flag=False
                break
    if flag:
        print('Yes')
    else:
        print('No')
