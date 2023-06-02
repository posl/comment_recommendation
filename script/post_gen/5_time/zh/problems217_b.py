Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读入数据
    s1 = input()
    s2 = input()
    s3 = input()
    # 列出所有可能的比赛
    all = ["ABC", "ARC", "AGC", "AHC"]
    # 删除已经输入的比赛
    all.remove(s1)
    all.remove(s2)
    all.remove(s3)
    # 打印答案
    print(all[0])
    return

=======
Suggestion 2

def main():
    s1 = input()
    s2 = input()
    s3 = input()

    if s1 == 'ABC':
        if s2 == 'ARC':
            print('AGC')
        else:
            print('ARC')
    elif s1 == 'ARC':
        if s2 == 'ABC':
            print('AGC')
        else:
            print('ABC')
    else:
        if s2 == 'ABC':
            print('ARC')
        else:
            print('ABC')

=======
Suggestion 3

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC' and s2 == 'ARC':
        print('AGC')
    elif s1 == 'ABC' and s2 == 'AGC':
        print('ARC')
    elif s1 == 'ARC' and s2 == 'ABC':
        print('AGC')
    elif s1 == 'ARC' and s2 == 'AGC':
        print('ABC')
    elif s1 == 'AGC' and s2 == 'ABC':
        print('ARC')
    elif s1 == 'AGC' and s2 == 'ARC':
        print('ABC')

=======
Suggestion 4

def get_missing(s1, s2, s3):
    if s1 == 'ABC':
        if s2 == 'ARC':
            return 'AGC'
        else:
            return 'ARC'
    elif s1 == 'ARC':
        if s2 == 'ABC':
            return 'AGC'
        else:
            return 'ABC'
    else:
        if s2 == 'ABC':
            return 'ARC'
        else:
            return 'ABC'

s1 = input()
s2 = input()
s3 = input()

print(get_missing(s1, s2, s3))

=======
Suggestion 5

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    if s1 == 'ABC' and s2 == 'ARC':
        print('AGC')
        return
    if s1 == 'ABC' and s2 == 'AGC':
        print('ARC')
        return
    if s1 == 'ARC' and s2 == 'ABC':
        print('AGC')
        return
    if s1 == 'ARC' and s2 == 'AGC':
        print('ABC')
        return
    if s1 == 'AGC' and s2 == 'ABC':
        print('ARC')
        return
    if s1 == 'AGC' and s2 == 'ARC':
        print('ABC')
        return
    if s1 == 'ABC' and s3 == 'ARC':
        print('AGC')
        return
    if s1 == 'ABC' and s3 == 'AGC':
        print('ARC')
        return
    if s1 == 'ARC' and s3 == 'ABC':
        print('AGC')
        return
    if s1 == 'ARC' and s3 == 'AGC':
        print('ABC')
        return
    if s1 == 'AGC' and s3 == 'ABC':
        print('ARC')
        return
    if s1 == 'AGC' and s3 == 'ARC':
        print('ABC')
        return
    if s2 == 'ABC' and s3 == 'ARC':
        print('AGC')
        return
    if s2 == 'ABC' and s3 == 'AGC':
        print('ARC')
        return
    if s2 == 'ARC' and s3 == 'ABC':
        print('AGC')
        return
    if s2 == 'ARC' and s3 == 'AGC':
        print('ABC')
        return
    if s2 == 'AGC' and s3 == 'ABC':
        print('ARC')
        return
    if s2 == 'AGC' and s3 == 'ARC':
        print('ABC')
        return
    return

=======
Suggestion 6

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    if "ABC" not in s:
        print("ABC")
    elif "ARC" not in s:
        print("ARC")
    elif "AGC" not in s:
        print("AGC")
    else:
        print("AHC")

=======
Suggestion 7

def main():
    S1 = input()
    S2 = input()
    S3 = input()
    if S1 == "ABC" and S2 == "ARC":
        print("AGC")
    elif S1 == "ARC" and S2 == "AGC":
        print("ABC")
    elif S1 == "AGC" and S2 == "ABC":
        print("ARC")
    elif S1 == "ABC" and S2 == "AHC":
        print("ARC")
    elif S1 == "AHC" and S2 == "ARC":
        print("ABC")
    elif S1 == "ARC" and S2 == "ABC":
        print("AHC")
    elif S1 == "AGC" and S2 == "AHC":
        print("ABC")
    elif S1 == "AHC" and S2 == "ABC":
        print("AGC")
    elif S1 == "ABC" and S2 == "ARC":
        print("AGC")
    elif S1 == "ARC" and S2 == "AGC":
        print("ABC")
    elif S1 == "AGC" and S2 == "ABC":
        print("ARC")
    elif S1 == "ABC" and S2 == "AHC":
        print("ARC")
    elif S1 == "AHC" and S2 == "ARC":
        print("ABC")
    elif S1 == "ARC" and S2 == "ABC":
        print("AHC")
    elif S1 == "AGC" and S2 == "AHC":
        print("ABC")
    elif S1 == "AHC" and S2 == "ABC":
        print("AGC")
    elif S1 == "ABC" and S2 == "ARC":
        print("AGC")
    elif S1 == "ARC" and S2 == "AGC":
        print("ABC")
    elif S1 == "AGC" and S2 == "ABC":
        print("ARC")
    elif S1 == "ABC" and S2 == "AHC":
        print("ARC")
    elif S1 == "AHC" and S2 == "ARC":
        print("ABC")
    elif S1 == "ARC" and S2 == "ABC":
        print("AHC")
    elif S1 == "AGC" and S2 == "

=======
Suggestion 8

def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    S = set([S_1, S_2, S_3])
    S_all = set(['ABC', 'ARC', 'AGC', 'AHC'])
    S_diff = S_all - S
    print(list(S_diff)[0])

=======
Suggestion 9

def main():
    s1 = input()
    s2 = input()
    s3 = input()
    s = [s1, s2, s3]
    l = ['ABC', 'ARC', 'AGC', 'AHC']
    for i in range(4):
        if l[i] not in s:
            print(l[i])
            break
