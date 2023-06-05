Synthesizing 10/10 solutions

=======
Suggestion 1

def get_index(s):
    if len(s) == 1:
        return ord(s) - ord('A') + 1
    else:
        count = 0
        for i in range(1, len(s)):
            count += 26 ** i
        count += ord(s[0]) - ord('A') + 1
        return count + get_index(s[1:])

=======
Suggestion 2

def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        ans += (ord(S[i])-ord('A')+1)*(26**(len(S)-i-1))
    print(ans)

=======
Suggestion 3

def get_index(s):
    index = 0
    for i in range(len(s)):
        index += (ord(s[i]) - ord('A') + 1) * (26 ** (len(s) - i - 1))
    return index

=======
Suggestion 4

def f(s):
    n = len(s)
    ans = 0
    for i in range(n):
        ans = ans * 26 + ord(s[i]) - ord('A') + 1
    return ans

s = input()
print(f(s))

=======
Suggestion 5

def get_num(s):
    if len(s) == 1:
        return ord(s) - ord('A') + 1
    else:
        return (ord(s[0]) - ord('A') + 1) * 26 ** (len(s) - 1) + get_num(s[1:])

=======
Suggestion 6

def main():
    S = input()
    #print(S)
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
    #print(S[68

=======
Suggestion 7

def convert(s):
    num = 0
    for i in range(len(s)):
        num *= 26
        num += ord(s[i]) - ord('A') + 1
    return num

print(convert(input()))

=======
Suggestion 8

def main():
    s = input()
    a = ord('A') - 1
    ans = 0
    for i in range(len(s)):
        ans += (ord(s[i]) - a) * (26 ** (len(s) - i - 1))
    print(ans)

=======
Suggestion 9

def get_num(s):
    if len(s) == 1:
        return ord(s) - 64
    else:
        return (ord(s[0]) - 64) * 26 + get_num(s[1:])

=======
Suggestion 10

def get_value(s):
    value = 0
    for i in range(len(s)):
        value += (ord(s[i])-ord('A')+1)*pow(26,len(s)-i-1)
    return value
# print(get_value('A'))
# print(get_value('B'))
# print(get_value('Z'))
# print(get_value('AA'))
# print(get_value('AB'))
# print(get_value('AZ'))
# print(get_value('BA'))
# print(get_value('BB'))
# print(get_value('ZZ'))
# print(get_value('AAA'))
# print(get_value('AAB'))
# print(get_value('AAZ'))
# print(get_value('ABA'))
# print(get_value('ABB'))
# print(get_value('ABZ'))
# print(get_value('ACA'))
# print(get_value('ACB'))
# print(get_value('ACZ'))
# print(get_value('AZZ'))
# print(get_value('BAA'))
# print(get_value('BAB'))
# print(get_value('BAZ'))
# print(get_value('BBA'))
# print(get_value('BBB'))
# print(get_value('BBZ'))
# print(get_value('BZZ'))
# print(get_value('ZAA'))
# print(get_value('ZAB'))
# print(get_value('ZAZ'))
# print(get_value('ZZZ'))
# print(get_value('AAAA'))
# print(get_value('AAAB'))
# print(get_value('AAAZ'))
# print(get_value('AABA'))
# print(get_value('AABB'))
# print(get_value('AABZ'))
# print(get_value('AACA'))
# print(get_value('AACB'))
# print(get_value('AACZ'))
# print(get_value('AAZZ'))
# print(get_value('ABAA'))
# print(get_value('ABAB'))
# print(get_value('ABAZ'))
# print(get_value('ABBA'))
# print(get_value('ABBB'))
# print(get_value('ABAZ'))
# print(get_value('ABBA'))
# print(get_value('ABBB'))
# print(get_value('ABZZ'))
# print(get_value('ACAA'))
# print(get_value('ACAB'))
# print(get_value('ACAZ'))
# print(get_value('ACBA'))
# print(get_value('ACBB'))
# print(get_value('ACBZ'))
# print(get_value('ACZA'))
# print(get_value('ACZB'))
# print(get_value('ACZZ'))
# print
