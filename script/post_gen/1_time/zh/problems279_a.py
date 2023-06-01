Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    print(S.count('wv'))

=======
Suggestion 2

def main():
    s = input()
    print(s.count('vw') + s.count('wv'))

=======
Suggestion 3

def count_bottoms(s):
    if s == 'v':
        return 1
    elif s == 'w':
        return 2
    else:
        return 0

s = input()
bottoms = 0
for i in range(len(s)):
    bottoms += count_bottoms(s[i])
print(bottoms)

=======
Suggestion 4

def main():
    S = input()
    print(S.count("wv"))

=======
Suggestion 5

def count_bottoms(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'w':
            count += s[i+1:].count('v')
    return count

=======
Suggestion 6

def print_count_of_bottoms(s):
    # 记录连续的v的个数
    count_of_v = 0
    # 记录底的个数
    count_of_bottoms = 0
    for c in s:
        if c == 'v':
            count_of_v += 1
        else:
            count_of_bottoms += count_of_v
    print(count_of_bottoms)

=======
Suggestion 7

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == "w":
            count += 1
            for j in range(i+1,len(s)):
                if s[j] == "v":
                    count += 1
                else:
                    break
    print(count)

=======
Suggestion 8

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == 'v':
            for j in range(i+1, len(s)):
                if s[j] == 'v':
                    count += 1
    print(count)
main()

=======
Suggestion 9

def main():
    s = input().strip()
    print(s.count('vv') + s.count('wv') * 2 + s.count('vw') * 2 + s.count('ww') * 3)

=======
Suggestion 10

def count_bottoms(s):
    """
    计算字符串s中的底的数量
    :param s: 一个由v和w组成的字符串
    :return: 底的数量
    """
    if len(s) == 1:
        return 1 if s == 'v' else 0
    else:
        return count_bottoms(s[0]) + count_bottoms(s[1:])
