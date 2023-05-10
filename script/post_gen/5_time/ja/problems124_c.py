Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    S = S.rstrip()
    S = S.lstrip()
    if len(S) == 1:
        print(0)
        return
    if len(S) == 2:
        if S[0] == S[1]:
            print(1)
            return
        else:
            print(0)
            return
    ret = 0
    for i in range(1,len(S)-1):
        if S[i-1] == S[i] and S[i] == S[i+1]:
            ret += 1
            if S[i] == '0':
                S = S[:i] + '1' + S[i+1:]
            else:
                S = S[:i] + '0' + S[i+1:]
    if S[0] == S[1]:
        ret += 1
    if S[len(S)-1] == S[len(S)-2]:
        ret += 1
    print(ret)

=======
Suggestion 2

def main():
    S = input()
    b = 0
    w = 0
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == '0':
                b += 1
            else:
                w += 1
        else:
            if S[i] == '0':
                w += 1
            else:
                b += 1
    print(min(b, w))

=======
Suggestion 3

def main():
    S = input()

    #print(S)

    #print(len(S))

    #print(S[0])

    #print(S[1])

    #print(S[2])

    #print(S[3])

    count = 0

    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == "1":
                count += 1
        else:
            if S[i] == "0":
                count += 1

    print(count)

=======
Suggestion 4

def main():
    s = input()
    #print(s)
    #print(len(s))
    #print(s[0])
    #print(s[1])
    #print(s[2])
    #print(s[3])
    #print(s[4])
    #print(s[5])
    #print(s[6])
    #print(s[7])
    #print(s[8])
    #print(s[9])
    #print(s[10])
    #print(s[11])
    #print(s[12])
    #print(s[13])
    #print(s[14])
    #print(s[15])
    #print(s[16])
    #print(s[17])
    #print(s[18])
    #print(s[19])
    #print(s[20])
    #print(s[21])
    #print(s[22])
    #print(s[23])
    #print(s[24])
    #print(s[25])
    #print(s[26])
    #print(s[27])
    #print(s[28])
    #print(s[29])
    #print(s[30])
    #print(s[31])
    #print(s[32])
    #print(s[33])
    #print(s[34])
    #print(s[35])
    #print(s[36])
    #print(s[37])
    #print(s[38])
    #print(s[39])
    #print(s[40])
    #print(s[41])
    #print(s[42])
    #print(s[43])
    #print(s[44])
    #print(s[45])
    #print(s[46])
    #print(s[47])
    #print(s[48])
    #print(s[49])
    #print(s[50])
    #print(s[51])
    #print(s[52])
    #print(s[53])
    #print(s[54])
    #print(s[55])
    #print(s[56])
    #print(s[57])
    #print(s[58])
    #print(s[59])
    #print(s[60])
    #print(s[61])
    #print(s[62])
    #print(s[63])
    #print(s[64])
    #print(s[65])
    #print(s[66])
    #print(s[67])
    #print(s[68

=======
Suggestion 5

def main():
    s = input()
    print(min(s.count('0'), s.count('1')) * 2)

=======
Suggestion 6

def main():
    S = input()
    count = 0
    for i in range(len(S)):
        if i % 2 == 0 and S[i] == '1':
            count += 1
        elif i % 2 == 1 and S[i] == '0':
            count += 1
    print(count)

=======
Suggestion 7

def main():
    #input
    S = input()
    #S = "10010010"

    #compute
    # 0,1の数を数える
    # 0,1の数が少ない方を選ぶ
    # 0,1の数が同じ場合は0を選ぶ
    # 1の数を数える
    # 0の数を数える
    # 0,1の数が少ない方を選ぶ
    # 0,1の数が同じ場合は1を選ぶ
    # 0,1の数が少ない方を選ぶ
    # 0,1の数が同じ場合は0を選ぶ
    # 0,1の数が少ない方を選ぶ
    # 0,1の数が同じ場合は1を選ぶ
    # 0,1の数が少ない方を選ぶ
    # 0,1の数が同じ場合は0を選ぶ
    # 0,1の数が少ない方を選ぶ
    # 0,1の数が同じ場合は1を選ぶ
    # 0,1の数が少ない方を選ぶ
    # 0,1の数が同じ場合は0を選ぶ
    # 0,1の数が少ない方を選ぶ
    # 0,1の数が同じ場合は1を選ぶ

    #output
    print(ans)

=======
Suggestion 8

def main():
    s = input()
    count0 = 0
    count1 = 0
    for i in range(len(s)):
        if s[i] == '0':
            count0 += 1
        else:
            count1 += 1
    print(min(count0, count1)*2)

=======
Suggestion 9

def main():
    S = input()
    count = 0

    for i in range(len(S)):
        if (i % 2 == 0 and S[i] == "1") or (i % 2 == 1 and S[i] == "0"):
            count += 1

    print(min(count, len(S) - count))

=======
Suggestion 10

def main():
    s = input()
    n = len(s)
    ans = min(s.count("0"), s.count("1"))
    print(ans * 2)
