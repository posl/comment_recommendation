Synthesizing 10/10 solutions

=======
Suggestion 1

def minPaints(s):
    #print(s)
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 0
    if len(s) == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 0
    if len(s) > 2:
        if s[0] == s[1]:
            return 1 + minPaints(s[2:])
        else:
            return minPaints(s[1:])

=======
Suggestion 2

def main():
    s = input()
    n = len(s)
    cnt = 0
    for i in range(n):
        if i % 2 == 0 and s[i] == '1':
            cnt += 1
        elif i % 2 == 1 and s[i] == '0':
            cnt += 1
    print(min(cnt, n-cnt))

=======
Suggestion 3

def solve(s):
    if len(s) == 1:
        return 0
    if len(s) == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 0
    count = 0
    for i in range(1, len(s) - 1):
        if s[i - 1] == s[i] and s[i] == s[i + 1]:
            count += 1
            s[i] = '0' if s[i] == '1' else '1'
    if s[0] == s[1]:
        count += 1
    if s[len(s) - 1] == s[len(s) - 2]:
        count += 1
    return count

=======
Suggestion 4

def main():
    s = input()
    n = len(s)
    count = 0
    for i in range(n):
        if i % 2 == 0 and s[i] == '1':
            count += 1
        elif i % 2 == 1 and s[i] == '0':
            count += 1
    print(min(count, n - count))

=======
Suggestion 5

def main():
    s = input()
    n = len(s)
    count = 0
    for i in range(n):
        if i % 2 == 0:
            if s[i] == '1':
                count += 1
        else:
            if s[i] == '0':
                count += 1
    print(min(count, n - count))

=======
Suggestion 6

def min_flip(S):
    # 从左到右，从右到左分别计算
    # 从左到右，如果当前字符和前一个字符相同，那么计数加1
    # 从右到左，如果当前字符和前一个字符相同，那么计数加1
    # 从左到右，从右到左，取最小值
    # 如果字符串长度为1，那么返回0
    if len(S) == 1:
        return 0
    count = 0
    for i in range(1,len(S)):
        if S[i] == S[i-1]:
            count += 1
    count2 = 0
    for i in range(len(S)-2,-1,-1):
        if S[i] == S[i+1]:
            count2 += 1
    return min(count,count2)

=======
Suggestion 7

def solve(s):
    s = list(s)
    if len(s) == 1:
        return 0
    if len(s) == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 0
    if len(s) == 3:
        if s[0] == s[1] and s[1] == s[2]:
            return 2
        elif s[0] == s[1] or s[1] == s[2] or s[0] == s[2]:
            return 1
        else:
            return 0
    res = 0
    for i in range(1, len(s)-1):
        if s[i] == s[i-1] and s[i] == s[i+1]:
            res += 1
            s[i] = str(1 - int(s[i]))
    if s[0] == s[1]:
        res += 1
        s[0] = str(1 - int(s[0]))
    if s[-1] == s[-2]:
        res += 1
        s[-1] = str(1 - int(s[-1]))
    return res

=======
Suggestion 8

def problem124_c():
    S = input()
    count = 0
    for i in range(len(S)):
        if i%2 == 0:
            if S[i] == '1':
                count += 1
        else:
            if S[i] == '0':
                count += 1
    print(count)

=======
Suggestion 9

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if (i % 2 == 0 and s[i] == '1') or (i % 2 == 1 and s[i] == '0'):
            count += 1
    print(min(count, len(s) - count))

=======
Suggestion 10

def solve(s):
    # 2种情况
    # 1. 第一个是0，最后一个是1
    # 2. 第一个是1，最后一个是0
    # 2种情况下，分别计算0和1的个数，取最小的那个
    # 0和1的个数计算方法是：从第一个开始，如果和前一个不一样，就+1
    # 需要注意的是，第一个和最后一个是特殊情况，需要单独判断
    # 最后，如果只有一个字符，返回0
    if len(s) == 1:
        return 0
    if s[0] == '0':
        count0 = 1
        count1 = 0
    else:
        count0 = 0
        count1 = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            if s[i] == '0':
                count0 += 1
            else:
                count1 += 1
    if s[0] == s[-1]:
        if s[0] == '0':
            count0 -= 1
        else:
            count1 -= 1
    return min(count0, count1)
