Synthesizing 10/10 solutions

=======
Suggestion 1

def get_index(s):
    if len(s) == 1:
        return ord(s) - ord('A') + 1
    else:
        return 26 * get_index(s[:-1]) + get_index(s[-1])

=======
Suggestion 2

def findIndex(s):
    # 1.找到s的长度
    # 2.根据s的长度，找到s所在的区间
    # 3.根据s的长度和所在区间，计算s的索引
    # 4.返回s的索引
    # 1.找到s的长度
    # 2.根据s的长度，找到s所在的区间
    # 3.根据s的长度和所在区间，计算s的索引
    # 4.返回s的索引
    # 1.找到s的长度
    # 2.根据s的长度，找到s所在的区间
    # 3.根据s的长度和所在区间，计算s的索引
    # 4.返回s的索引
    # 1.找到s的长度
    # 2.根据s的长度，找到s所在的区间
    # 3.根据s的长度和所在区间，计算s的索引
    # 4.返回s的索引
    # 1.找到s的长度
    # 2.根据s的长度，找到s所在的区间
    # 3.根据s的长度和所在区间，计算s的索引
    # 4.返回s的索引
    # 1.找到s的长度
    # 2.根据s的长度，找到s所在的区间
    # 3.根据s的长度和所在区间，计算s的索引
    # 4.返回s的索引
    # 1.找到s的长度
    # 2.根据s的长度，找到s所在的区间
    # 3.根据s的长度和所在区间，计算s的索引
    # 4.返回s的索引
    # 1.找到s的长度
    # 2.根据s的长度，找到s所

=======
Suggestion 3

def get_index(s):
    index = 0
    for i in range(1, len(s)):
        index += 26 ** i
    for i in range(1, len(s)):
        index += 26 ** i * (ord(s[i]) - ord('A') - 1)
    index += ord(s[0]) - ord('A')
    return index + 1

=======
Suggestion 4

def get_index(s):
    index = 0
    for i in range(len(s)):
        index += (ord(s[i]) - 64) * 26 ** i
    return index

print(get_index(input()))

=======
Suggestion 5

def get_num(s):
    num = 0
    for i in range(len(s)):
        num += (ord(s[i]) - 64) * (26 ** (len(s) - i - 1))
    return num

s = input()
print(get_num(s))

=======
Suggestion 6

def get_index(s):
    # 1 - 26
    # 27 - 702
    # 703 - 18278
    # 18279 - 475254
    # 475255 - 12356630
    # 12356631 - 321272406
    # 321272407 - 8353082582
    # 8353082583 - 217180147158
    # 217180147159 - 5646683826134
    # 5646683826135 - 146813779479510
    # 146813779479511 - 3813670440297310
    # 3813670440297311 - 99035203142830460
    # 99035203142830461 - 2577687858367758005
    # 2577687858367758006 - 66830852109000000000
    if len(s) == 1:
        return ord(s) - 64
    elif len(s) == 2:
        return (ord(s[0]) - 64) * 26 + (ord(s[1]) - 64)
    else:
        return (ord(s[0]) - 64) * 26 + (ord(s[1]) - 64) + (ord(s[2]) - 64) * 26 * 26

=======
Suggestion 7

def get_index(s):
    count = 0
    for i in range(len(s)):
        count += (26 ** (i + 1))
    return count

=======
Suggestion 8

def convert(s):
    n = len(s)
    if n == 1:
        return ord(s) - 65 + 1
    else:
        return 26 * (n - 1) + convert(s[:-1]) * 26 + ord(s[-1]) - 65 + 1

print(convert(input()))

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def get_index(s):
    if len(s) == 1:
        return ord(s) - ord('A') + 1
    else:
        if len(s) == 2:
            return 26 + get_index(s[1])
        else:
            return 26 + 26 + get_index(s[2:])
