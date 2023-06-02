Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    S = input()
    print(len(set(S)))

=======
Suggestion 2

def main():
    s = input()
    #print(s)
    #print(len(s))
    set_s = set(s)
    #print(set_s)
    #print(len(set_s))
    #print(len(s)-len(set_s))
    if len(s)-len(set_s) == 0:
        print(6)
    elif len(s)-len(set_s) == 1:
        print(3)
    else:
        print(1)
    return 0

=======
Suggestion 3

def main():
    s = input()
    print(len(set(s)))

=======
Suggestion 4

def permutation(n):
    if len(n) <= 1:
        return [n]
    else:
        result = []
        for i in range(len(n)):
            for j in permutation(n[:i] + n[i+1:]):
                result.append(n[i:i+1] + j)
        return result

=======
Suggestion 5

def main():
    # 读取输入
    S = input()
    # 用集合去重
    S_set = set(S)
    # 集合中元素个数
    S_set_len = len(S_set)
    # 用数学公式计算排列组合
    result = S_set_len * (S_set_len - 1) * (S_set_len - 2)
    # 打印输出
    print(result)

=======
Suggestion 6

def swap(c1, c2):
    tmp = c1
    c1 = c2
    c2 = tmp
    return c1, c2

=======
Suggestion 7

def main():
    s = input()
    n = len(s)
    a = 1
    for i in range(1, n+1):
        a *= i
    print(a)

=======
Suggestion 8

def permute(s):
    if len(s) == 1:
        return [s]
    permutations = []
    for i, c in enumerate(s):
        for p in permute(s[:i] + s[i+1:]):
            permutations.append(c + p)
    return permutations

S = input()
print(len(permute(S)))

=======
Suggestion 9

def solution():
    s = input()
    a = s[0]
    b = s[1]
    c = s[2]
    if a == b == c:
        print(1)
    elif a == b or a == c or b == c:
        print(3)
    else:
        print(6)

=======
Suggestion 10

def main():
    S = input()
    print(len(set(S)))
