Synthesizing 10/10 solutions

=======
Suggestion 1

def get_index(s):
    result = 0
    for i in range(len(s)):
        result += (ord(s[i]) - ord('A') + 1) * 26 ** (len(s) - i - 1)
    return result

=======
Suggestion 2

def get_index(s):
    if len(s) == 1:
        return ord(s) - ord('A') + 1
    else:
        return 26 * get_index(s[:-1]) + ord(s[-1]) - ord('A') + 1

=======
Suggestion 3

def get_index(s):
    l = len(s)
    if l == 1:
        return ord(s) - ord('A') + 1
    else:
        index = 0
        for i in range(l-1):
            index += 26 ** (i+1)
        return index + get_index(s[1:]) + 1

=======
Suggestion 4

def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        ans = ans * 26 + ord(S[i]) - ord('A') + 1
    print(ans)

=======
Suggestion 5

def getNum(s):
    res = 0
    for i in range(len(s)):
        res = res * 26 + ord(s[i]) - ord('A') + 1
    return res

=======
Suggestion 6

def get_num(s):
    num = 0
    for i in range(len(s)):
        num += (ord(s[i])-64)*26**(len(s)-i-1)
    return num

print(get_num(input()))

=======
Suggestion 7

def main():
    # 读取输入
    s = input()
    # 计算
    ans = 0
    for i in range(len(s)):
        if i == 0:
            ans += (ord(s[i]) - ord('A')) + 1
        else:
            ans += (ord(s[i]) - ord('A')) * 26 ** i + 1
    # 输出
    print(ans)

=======
Suggestion 8

def findWord(word):
    if len(word) == 1:
        return ord(word) - 64
    else:
        count = 0
        for i in range(len(word)):
            count += (ord(word[i]) - 64) * 26 ** (len(word) - i - 1)
        return count

=======
Suggestion 9

def get_index(s):
    index = 0
    for i in range(len(s)):
        index += (ord(s[i])-ord('A')+1)*(26**(len(s)-i-1))
    return index

=======
Suggestion 10

def get_index(s):
    index = 0
    for i in range(len(s)):
        index = index * 26 + (ord(s[i]) - ord('A') + 1)
    return index
