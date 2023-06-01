Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读取输入
    s = input()
    # 用一个字典记录每个字符出现的次数
    count = {}
    for c in s:
        if c not in count:
            count[c] = 0
        count[c] += 1
    # 如果只有两种字符，并且每种字符都出现了两次，则打印Yes
    if len(count) == 2 and all([count[c] == 2 for c in count]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s = input()
    if len(set(s)) == 2:
        if s.count(s[0]) == 2 and s.count(s[1]) == 2:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    if len(s) == 4:
        if s[0] == s[1] and s[2] == s[3]:
            print("Yes")
        elif s[0] == s[2] and s[1] == s[3]:
            print("Yes")
        elif s[0] == s[3] and s[1] == s[2]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
main()

=======
Suggestion 4

def main():
    s = input()
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    if len(d) == 2:
        for v in d.values():
            if v != 2:
                print('No')
                return
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    s = input()
    if len(set(s)) == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def isTwoCharacter(s):
    if len(s) != 4:
        return False
    if len(set(s)) == 2:
        for c in set(s):
            if s.count(c) != 2:
                return False
        return True
    else:
        return False

=======
Suggestion 7

def main():
    S = input()
    if len(S) != 4:
        print("No")
        return
    if S[0] == S[1] and S[2] == S[3] and S[0] != S[2]:
        print("Yes")
        return
    if S[0] == S[2] and S[1] == S[3] and S[0] != S[1]:
        print("Yes")
        return
    if S[0] == S[3] and S[1] == S[2] and S[0] != S[1]:
        print("Yes")
        return
    print("No")

=======
Suggestion 8

def main():
    s = input()
    if len(s) != 4:
        return
    if len(set(s)) != 2:
        return
    for c in set(s):
        if s.count(c) != 2:
            return
    print("Yes")

=======
Suggestion 9

def main():
    s = input()
    if len(s) != 4:
        print("No")
        return
    s = sorted(s)
    if s[0] == s[1] and s[2] == s[3] and s[0] != s[2]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    S = input()
    if len(S) == 4:
        if S.count(S[0]) == 2 and S.count(S[1]) == 2 and S.count(S[2]) == 2 and S.count(S[3]) == 2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
