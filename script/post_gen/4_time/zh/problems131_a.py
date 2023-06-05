Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    import sys
    S = sys.stdin.readline().strip()
    if S[0] == S[1] == S[2] == S[3]:
        print("Bad")
    elif S[0] == S[1] and S[2] == S[3]:
        print("Bad")
    elif S[0] == S[2] and S[1] == S[3]:
        print("Bad")
    elif S[0] == S[3] and S[1] == S[2]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 2

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        print("Bad")
    elif s[0] == s[1] and s[1] == s[2]:
        print("Bad")
    elif s[1] == s[2] and s[2] == s[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 3

def main():
    # 读取输入
    s = input()

    # 初始化
    ans = 'Good'

    # 处理
    if s[0] == s[1] and s[1] == s[2] and s[2] == s[3]:
        ans = 'Bad'

    # 输出结果
    print(ans)

=======
Suggestion 4

def problems131_a():
    s = input()
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 5

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2] or s[1] == s[2] and s[2] == s[3]:
        print('Bad')
    else:
        print('Good')

=======
Suggestion 6

def main():
    s = input()
    if s[0] == s[1] == s[2] == s[3]:
        print("Bad")
    elif s[1] == s[2] == s[3]:
        print("Bad")
    elif s[0] == s[1] == s[2]:
        print("Bad")
    else:
        print("Good")

=======
Suggestion 7

def main():
    # 读取输入
    input = raw_input()
    # 处理输入
    # 通过if-else语句处理
    # 假设输入为input
    if input[0] == input[1] and input[1] == input[2] and input[2] == input[3]:
        print "Bad"
    else:
        print "Good"
    # 输出结果
