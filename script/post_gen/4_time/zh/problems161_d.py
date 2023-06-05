Synthesizing 9/10 solutions

=======
Suggestion 1

def get_num(k):
    list = []
    i = 1
    while True:
        if i % 10 == 0:
            i += 1
            continue
        list.append(i)
        i += 1
        if len(list) == k:
            break
    return list[-1]

=======
Suggestion 2

def check(x):
    if x < 10:
        return True
    if x < 100:
        return abs(x // 10 - x % 10) <= 1
    return abs(x // 10 % 10 - x % 10) <= 1 and check(x // 10)

=======
Suggestion 3

def check(num):
    num = str(num)
    if len(num) == 1:
        return True
    for i in range(len(num) - 1):
        if abs(int(num[i]) - int(num[i + 1])) > 1:
            return False
    return True

=======
Suggestion 4

def check(num):
    num = str(num)
    for i in range(len(num)-1):
        if abs(int(num[i]) - int(num[i+1])) > 1:
            return False
    return True

=======
Suggestion 5

def main():
    #print("问题陈述\n当且仅当以下条件得到满足时，一个正整数X被认为是一个朗朗上口的数字：\n在X的十进制表示中（不含前导零），对于每一对相邻的数字，这些数字的绝对差值最多为1。\n例如，1234、1和334都是仑数，而31415、119和13579都不是。\n给你一个正整数K，找出第K个最小的伦常数。\n\n限制条件\n1 ≦ K ≦ 10^5\n输入的所有数值都是整数。\n\n输入\n输入由标准输入提供，格式如下：\nK\n\n輸出\n打印答案。\n\n输入样本1\n15\n\n样本输出1\n23\n我们将按升序列出15个最小的朗朗上口数字：\n1,\n2,\n3,\n4,\n5,\n6,\n7,\n8,\n9,\n10,\n11,\n12,\n21,\n22,\n23.\n因此，答案是23。\n\n输入样本2\n1\n\n样本输出2\n1\n\n样品输入3\n13\n\n样品输出3\n21\n\n样本输入4\n100000\n\n样本输出4\n3234566667\n注意，答案可能不适合32位有符号整数类型。")
    k = int(input())
    count = 0
    i = 1
    while True:
        if i < 10:
            count += 1
        else:
            s = str(i)
            flag = True
            for j in range(len(s)-1):
                if abs(int(s[j]) - int(s[j+1])) > 1:
                    flag = False
                    break
            if flag:
                count += 1
        if count == k:
            print(i)
            break
        i += 1
    return 0

=======
Suggestion 6

def isLuckyNumber(x):
    if x < 10:
        return True
    else:
        x = str(x)
        for i in range(0, len(x)-1):
            if abs(int(x[i])-int(x[i+1])) > 1:
                return False
        return True

K = int(input())
count = 0
i = 0
while count < K:
    i += 1
    if isLuckyNumber(i):
        count += 1
print(i)

=======
Suggestion 7

def isLuckyNumber(n):
    if n < 10:
        return True
    else:
        while n > 9:
            n1 = n % 10
            n2 = n // 10 % 10
            if abs(n1 - n2) > 1:
                return False
            n = n // 10
        return True

=======
Suggestion 8

def is_good(n):
    s = str(n)
    for i in range(1, len(s)):
        if abs(int(s[i]) - int(s[i - 1])) > 1:
            return False
    return True

=======
Suggestion 9

def isLunLun(num):
    num = str(num)
    for i in range(1, len(num)):
        if abs(int(num[i-1]) - int(num[i])) > 1:
            return False
    return True
