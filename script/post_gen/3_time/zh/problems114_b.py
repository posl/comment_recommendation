Synthesizing 10/10 solutions

=======
Suggestion 1

def get_min_diff(s):
    min_diff = 1000
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        diff = abs(x-753)
        if diff < min_diff:
            min_diff = diff
    return min_diff

=======
Suggestion 2

def get_min_diff(s):
    min_diff = 999
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        diff = abs(753-x)
        if diff < min_diff:
            min_diff = diff
    return min_diff

=======
Suggestion 3

def main():
    #输入
    S = input()
    #初期化
    min_diff = 999
    #逐个取出三个连续的数字
    for i in range(len(S)-2):
        #取出数字
        X = int(S[i:i+3])
        #计算与753的差值
        diff = abs(X-753)
        #更新最小值
        if diff < min_diff:
            min_diff = diff
    #输出
    print(min_diff)

=======
Suggestion 4

def min_diff(S):
    min_diff = 999
    for i in range(len(S)-2):
        x = int(S[i:i+3])
        diff = abs(753 - x)
        if diff < min_diff:
            min_diff = diff
    return min_diff

=======
Suggestion 5

def main():
    S = input()
    min_diff = 1000
    for i in range(len(S)-2):
        diff = abs(753 - int(S[i:i+3]))
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 6

def main():
    s = input()
    print(min(abs(int(s[i:i+3])-753) for i in range(len(s)-2)))

=======
Suggestion 7

def main():
    S = input()
    N = len(S)
    min_diff = 1e9
    for i in range(N-2):
        x = int(S[i:i+3])
        diff = abs(753 - x)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 8

def main():
    S = input()
    S = list(S)
    S = list(map(int, S))
    min_diff = 1000
    for i in range(len(S)-2):
        X = S[i]*100 + S[i+1]*10 + S[i+2]
        diff = abs(X-753)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 9

def main():
    s = input()
    sub = 1000
    for i in range(len(s)-2):
        x = int(s[i:i+3])
        sub = min(sub,abs(753-x))
    print(sub)

=======
Suggestion 10

def get_num(s):
    if len(s) == 3:
        return int(s)
    else:
        return int(s[0:3])

s = input()
min_diff = 1000
for i in range(len(s)-2):
    diff = abs(get_num(s[i:i+3]) - 753)
    if diff < min_diff:
        min_diff = diff

print(min_diff)
