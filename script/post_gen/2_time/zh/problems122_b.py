Synthesizing 10/10 solutions

=======
Suggestion 1

def problem122_b(s):
    #print(s)
    s = s.replace('A','1')
    s = s.replace('C','2')
    s = s.replace('G','3')
    s = s.replace('T','4')
    #print(s)
    s = s.replace('1','A')
    s = s.replace('2','C')
    s = s.replace('3','G')
    s = s.replace('4','T')
    #print(s)
    max_len = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            #print(s[i:j])
            if s[i:j].find('B') == -1 and s[i:j].find('D') == -1 and s[i:j].find('E') == -1 and s[i:j].find('F') == -1 and s[i:j].find('H') == -1 and s[i:j].find('I') == -1 and s[i:j].find('J') == -1 and s[i:j].find('K') == -1 and s[i:j].find('L') == -1 and s[i:j].find('M') == -1 and s[i:j].find('N') == -1 and s[i:j].find('O') == -1 and s[i:j].find('P') == -1 and s[i:j].find('Q') == -1 and s[i:j].find('R') == -1 and s[i:j].find('S') == -1 and s[i:j].find('U') == -1 and s[i:j].find('V') == -1 and s[i:j].find('W') == -1 and s[i:j].find('X') == -1 and s[i:j].find('Y') == -1 and s[i:j].find('Z') == -1:
                max_len = max(max_len,len(s[i:j]))
    print(max_len)

=======
Suggestion 2

def getLongestACGT(s):
    longestACGT = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            if isACGT(s[i:j+1]):
                if longestACGT < (j-i+1):
                    longestACGT = (j-i+1)
    return longestACGT

=======
Suggestion 3

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            ok = True
            for k in range(i, j + 1):
                if s[k] != 'A' and s[k] != 'C' and s[k] != 'G' and s[k] != 'T':
                    ok = False
            if ok:
                ans = max(ans, j - i + 1)
    print(ans)

=======
Suggestion 4

def get_length(s):
    length = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if is_acgt(s[i:j]):
                length = max(length, j-i)
    return length

=======
Suggestion 5

def main():
    s = input()
    ans = 0
    cnt = 0
    for i in range(len(s)):
        if s[i] == "A" or s[i] == "C" or s[i] == "G" or s[i] == "T":
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    ans = 0
    cnt = 0
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
            cnt += 1
        else:
            ans = max(cnt, ans)
            cnt = 0
    print(ans)

=======
Suggestion 7

def main():
    # 读入字符串
    S = input()
    # 计数
    count = 0
    # 长度
    length = 0
    # 遍历字符串
    for i in range(len(S)):
        # 如果是ACGT的话
        if S[i] == 'A' or S[i] == 'C' or S[i] == 'G' or S[i] == 'T':
            # 计数加一
            count += 1
            # 如果长度小于计数的话
            if length < count:
                # 长度等于计数
                length = count
        # 如果不是ACGT的话
        else:
            # 计数等于0
            count = 0
    # 输出长度
    print(length)

=======
Suggestion 8

def main():
    s = input()
    print(s)
    print(len(s))
    print('hello world')

=======
Suggestion 9

def main():
    S = input()
    max_len = 0
    for i in range(len(S)):
        for j in range(i+1, len(S)+1):
            if is_acgt(S[i:j]):
                max_len = max(max_len, j-i)
    print(max_len)

=======
Suggestion 10

def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            ok = True
            for k in range(i, j+1):
                if s[k] != 'A' and s[k] != 'C' and s[k] != 'G' and s[k] != 'T':
                    ok = False
            if ok:
                ans = max(ans, j-i+1)
    print(ans)
