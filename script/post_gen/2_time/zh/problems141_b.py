Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    for i in range(len(s)):
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
Suggestion 2

def main():
    s = input()
    for i in range(len(s)):
        if (i + 1) % 2 == 1:
            if s[i] not in ['R', 'U', 'D']:
                print('No')
                return
        else:
            if s[i] not in ['L', 'U', 'D']:
                print('No')
                return
    print('Yes')

=======
Suggestion 3

def judge_easy(s):
    if len(s) == 1:
        return True
    #奇数位置
    for i in range(0, len(s), 2):
        if s[i] in ['L', 'D']:
            return False
    #偶数位置
    for i in range(1, len(s), 2):
        if s[i] in ['R', 'D']:
            return False
    return True

=======
Suggestion 4

def is_easy_to_play(str):
    is_even_pos = True
    for c in str:
        if is_even_pos:
            if c == 'L':
                return False
        else:
            if c == 'R':
                return False
        is_even_pos = not is_even_pos
    return True

=======
Suggestion 5

def is_easy(s):
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == 'L':
                return 'No'
        else:
            if s[i] == 'R':
                return 'No'
    return 'Yes'

=======
Suggestion 6

def func(s):
    if len(s) % 2 == 1:
        return 'No'
    else:
        if s[0] == 'L' or s[len(s) - 1] == 'L':
            return 'No'
        else:
            for i in range(0, len(s), 2):
                if s[i] == 'L':
                    return 'No'
            for i in range(1, len(s), 2):
                if s[i] != 'L':
                    return 'No'
            return 'Yes'

=======
Suggestion 7

def main():
    S = input()
    odd = S[::2]
    even = S[1::2]
    if odd == odd.upper() and even == even.lower():
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    s = input()
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == 'L':
                print('No')
                exit(0)
        else:
            if s[i] == 'R':
                print('No')
                exit(0)
    print('Yes')

main()

=======
Suggestion 9

def main():
    # 读入字符串
    S = input()
    # 奇数位置（第1个、第3个、第5个......）上的每个字符都是R、U或D。
    # 偶数位置（第2，4，6，...）的每个字符是L，U或D。
    # 从第一个位置开始，判断奇数位置是否为RUD，偶数位置是否为LUD
    result = "Yes"
    for index in range(len(S)):
        if index % 2 == 0:
            if S[index] == "L":
                result = "No"
                break
        else:
            if S[index] == "R":
                result = "No"
                break
    print(result)
    return

=======
Suggestion 10

def is_easy_dance(s):
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == 'L':
                return False
        else:
            if s[i] == 'R':
                return False
    return True
