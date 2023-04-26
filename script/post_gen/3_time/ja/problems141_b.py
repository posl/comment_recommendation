Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0::2].count('R') + s[0::2].count('U') + s[0::2].count('D') == len(s[0::2]) and s[1::2].count('L') + s[1::2].count('U') + s[1::2].count('D') == len(s[1::2]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    if S[::2].count('R') + S[::2].count('U') + S[::2].count('D') == len(S[::2]) and S[1::2].count('L') + S[1::2].count('U') + S[1::2].count('D') == len(S[1::2]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    if s[::2].count('L') == 0 and s[1::2].count('R') == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    s = input()
    if s[::2].count("L") == 0 and s[1::2].count("R") == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    s = input()
    if s[0::2].count('L') == 0 and s[1::2].count('R') == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    s = input()
    if s[0] == 'R' or s[0] == 'U' or s[0] == 'D':
        for i in range(1,len(s)):
            if i % 2 == 0:
                if s[i] == 'L' or s[i] == 'U' or s[i] == 'D':
                    continue
                else:
                    print('No')
                    break
            else:
                if s[i] == 'R' or s[i] == 'U' or s[i] == 'D':
                    continue
                else:
                    print('No')
                    break
        else:
            print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    s = input()
    for i in range(0,len(s),2):
        if s[i] in "L":
            print("No")
            exit()
    for i in range(1,len(s),2):
        if s[i] in "R":
            print("No")
            exit()
    print("Yes")

=======
Suggestion 8

def main():
    S = input()
    ans = 'Yes'
    for i in range(0,len(S),2):
        if S[i] in 'RL':
            ans = 'No'
            break
    for i in range(1,len(S),2):
        if S[i] in 'UD':
            ans = 'No'
            break
    print(ans)

=======
Suggestion 9

def main():
    S = input()
    if len(S)%2 == 1:
        print("No")
    else:
        if S[0::2].count("R") + S[0::2].count("U") + S[0::2].count("D") == len(S[0::2]) and S[1::2].count("L") + S[1::2].count("U") + S[1::2].count("D") == len(S[1::2]):
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def main():
    s = input()
    #print('s =', s)
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
    #
