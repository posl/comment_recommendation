Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    ans = 753
    for i in range(len(S)-2):
        ans = min(ans, abs(753 - int(S[i:i+3])))
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    ans = 753
    for i in range(len(s)-2):
        ans = min(ans, abs(753-int(s[i:i+3])))
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    min = 1000
    for i in range(len(S)-2):
        X = int(S[i:i+3])
        if abs(X-753) < min:
            min = abs(X-753)
    print(min)

=======
Suggestion 4

def main():
    s = input()
    ans = 1000
    for i in range(len(s) - 2):
        x = abs(753 - int(s[i:i + 3]))
        if x < ans:
            ans = x
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    min = 753
    for i in range(len(S)-2):
        if abs(753-int(S[i:i+3])) < min:
            min = abs(753-int(S[i:i+3]))
    print(min)

=======
Suggestion 6

def main():
    S = input()
    num = 753
    ans = 1000
    for i in range(len(S)-2):
        ans = min(ans, abs(num - int(S[i:i+3])))
    print(ans)

=======
Suggestion 7

def main():
    S = input()
    #print(S)
    #print(type(S))
    #print(len(S))
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print(S[4])
    #print(S[5])
    #print(S[6])
    #print(S[7])
    #print(S[8])
    #print(S[9])
    #print(S[10])
    #print(S[11])
    #print(S[12])
    #print(S[13])
    #print(S[14])
    #print(S[15])
    #print(S[16])
    #print(S[17])
    #print(S[18])
    #print(S[19])
    #print(S[20])
    #print(S[21])
    #print(S[22])
    #print(S[23])
    #print(S[24])
    #print(S[25])
    #print(S[26])
    #print(S[27])
    #print(S[28])
    #print(S[29])
    #print(S[30])
    #print(S[31])
    #print(S[32])
    #print(S[33])
    #print(S[34])
    #print(S[35])
    #print(S[36])
    #print(S[37])
    #print(S[38])
    #print(S[39])
    #print(S[40])
    #print(S[41])
    #print(S[42])
    #print(S[43])
    #print(S[44])
    #print(S[45])
    #print(S[46])
    #print(S[47])
    #print(S[48])
    #print(S[49])
    #print(S[50])
    #print(S[51])
    #print(S[52])
    #print(S[53])
    #print(S[54])
    #print(S[55])
    #print(S[56])
    #print(S[57])
    #print(S[58])
    #print(S[59])
    #print(S[60])
    #print(S[61])
    #print(S[62])
    #print(S[63])
    #print(S[64])
    #print(S[65])
    #print(S[66])
    #print(S[67])

=======
Suggestion 8

def main():
    S = input()
    S = S.replace(" ", "")
    S = S.replace("

", "")
    if len(S) < 4:
        print(753 - int(S))
    else:
        min = 753 - int(S[0:3])
        for i in range(len(S) - 2):
            if min > 753 - int(S[i:i+3]):
                min = 753 - int(S[i:i+3])
        print(min)

=======
Suggestion 9

def main():
    # 1行目
    S = input()
    # 3文字ずつ取り出す
    S3 = [S[i:i+3] for i in range(len(S)-2)]
    # 3文字の差の絶対値を求める
    diff = [abs(int(s)-753) for s in S3]
    # 最小値を出力
    print(min(diff))

=======
Suggestion 10

def main():
    S = input()
    S = S.replace(""," ")
    S = S.split()
    S = list(
