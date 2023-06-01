Synthesizing 10/10 solutions

=======
Suggestion 1

def get_num(s):
    # 先计算出所有的字母组合
    # 1个字母组合 26
    # 2个字母组合 26*26
    # 3个字母组合 26*26*26
    # 4个字母组合 26*26*26*26
    # 5个字母组合 26*26*26*26*26
    # 6个字母组合 26*26*26*26*26*26
    # 7个字母组合 26*26*26*26*26*26*26
    # 8个字母组合 26*26*26*26*26*26*26*26
    # 9个字母组合 26*26*26*26*26*26*26*26*26
    # 10个字母组合 26*26*26*26*26*26*26*26*26*26
    # 11个字母组合 26*26*26*26*26*26*26*26*26*26*26
    # 12个字母组合 26*26*26*26*26*26*26*26*26*26*26*26
    # 13个字母组合 26*26*26*26*26*26*26*26*26*26*26*26*26
    # 14个字母组合 26*26*26*26*26*26*26*26*26*26*26*26*26*26
    # 15个字母组合 26*26*26*26*26*26*26*26*26*2

=======
Suggestion 2

def get_index(s):
    n = len(s)
    if n == 1:
        return ord(s) - ord('A') + 1
    elif n == 2:
        return 26 + (ord(s[0]) - ord('A')) * 26 + (ord(s[1]) - ord('A')) + 1
    else:
        return 26 + 26 * 26 + (ord(s[0]) - ord('A')) * 26 * 26 + (ord(s[1]) - ord('A')) * 26 + (ord(s[2]) - ord('A')) + 1

=======
Suggestion 3

def get_index(id):
    # 长度为1的字符串，有26个，按词法顺序排列，因此前26个的索引为1-26
    # 长度为2的字符串，有26*26个，按词法顺序排列，因此前26*26个的索引为27-26*26+26
    # 长度为3的字符串，有26*26*26个，按词法顺序排列，因此前26*26*26个的索引为26*26+26*26*26+26
    # 长度为n的字符串，有26*26*26*...*26个，按词法顺序排列，因此前26*26*26*...*26个的索引为26*26*26*...*26+26
    # 总结：长度为n的字符串，前面有26*26*26*...*26个，因此前26*26*26*...*26个的索引为26*26*26*...*26+26
    # 因此，长度为n的字符串，前面有26*26*26*...*26个，因此前26*26*26*...*26个的索引为26*26*26*...*26+26
    # 因此，长度为n的字符串，前面有26*26*26*...*26个，因此前26*26*26*...*26个的索引为26*26*26*...*26+26
    # 因此，长度为n的字符串，前面有26*26*26*...*26个，因此前26*26*26*...*26个的索引为26*26*26*...*26+26
    # 因此，长度为n的字符串，前面有26*26*26*...*26个，因此前26*26*26*...*26个的索引为26*26*26*...*26+26

    # 从第一位开始，每一位都有26种可能，因此第

=======
Suggestion 4

def main():
    s = input()
    # 1. 确定长度
    # 2. 确定首字母
    # 3. 确定余下的字母
    # 4. 确定排列顺序
    # 5. 确定索引
    # 6. 打印
    # 1. 确定长度
    length = len(s)
    # 2. 确定首字母
    first = s[0]
    # 3. 确定余下的字母
    if length == 1:
        rest = 0
    else:
        rest = int(s[1:])
    # 4. 确定排列顺序
    # 5. 确定索引
    # 6. 打印
    print((ord(first) - 64) * (26 ** (length - 1)) + rest)

main()

=======
Suggestion 5

def problem285_c():
    s = input()
    length = len(s)
    sum = 0
    for i in range(length):
        sum += (ord(s[i])-ord('A')+1)*(26**(length-i-1))
    print(sum)

=======
Suggestion 6

def main():
    S = input()
    l = len(S)
    n = 0
    for i in range(l):
        n = n*26 + ord(S[i]) - 64
    print(n)

=======
Suggestion 7

def problems285_c():
    s = input()
    sum = 0
    for i in range(1,len(s)):
        sum += 26 ** i
    sum += (ord(s[0]) - 64) * 26 ** (len(s) - 1)
    print(sum)

problems285_c()

=======
Suggestion 8

def find_index(s):
    # 用26进制的思想
    index = 0
    for i in range(len(s)):
        index = index * 26 + ord(s[i]) - ord('A') + 1
    return index

=======
Suggestion 9

def get_index_of_problem(problem_id):
    index = 0
    for i in range(len(problem_id)):
        index += (ord(problem_id[i]) - ord('A') + 1) * 26 ** (len(problem_id) - 1 - i)
    return index

=======
Suggestion 10

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        ans = ans * 26 + ord(s[i]) - ord('A') + 1
    print(ans)
