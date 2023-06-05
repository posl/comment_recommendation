Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    print(len(set(S)))

=======
Suggestion 2

def main():
    s = input()
    print(len(set(s)))

=======
Suggestion 3

def problems225_a():
    s = input()
    print(len(set(s)))

=======
Suggestion 4

def main():
    s = input()
    print(len(s) * (len(s) - 1) * (len(s) - 2) // 6)

=======
Suggestion 5

def main():
    S = input()
    l = list(S)
    l1 = []
    for i in range(len(l)):
        if l[i] not in l1:
            l1.append(l[i])
    print(len(l1))

=======
Suggestion 6

def problem225_a():
    s = input()
    print(len(set(s)))

=======
Suggestion 7

def problems225_a():
    S = input()
    print(len(set(S)))

=======
Suggestion 8

def main():
    # 读取输入
    s = input()
    # 通过交换S中的字符可以得到的不同字符串的数量。
    print(len(set(s)))

=======
Suggestion 9

def main():
    # 读入字符串
    s = input()
    # 用set来存储排列组合后的字符串
    s_set = set()
    # 遍历s的所有排列组合
    for i in range(len(s)):
        for j in range(len(s)):
            for k in range(len(s)):
                s_set.add(s[i] + s[j] + s[k])
    # 输出set的大小
    print(len(s_set))
