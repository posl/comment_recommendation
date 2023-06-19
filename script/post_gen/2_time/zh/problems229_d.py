Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    K = int(input())
    l = len(S)
    #print(l)
    #print(K)
    #pr

=======
Suggestion 2

def solve():
    s = input()
    k = int(input())
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == 'X':
            ans += 1
        elif k > 0 and (i == 0 or s[i - 1] != 'X') and (i == n - 1 or s[i + 1] != 'X'):
            ans += 1
            k -= 1
    print(ans)

=======
Suggestion 3

def solve(s, k):
    n = len(s)
    max_consecutive_x = 0
    consecutive_x = 0
    for i in range(n):
        if s[i] == 'X':
            consecutive_x += 1
        else:
            max_consecutive_x = max(max_consecutive_x, consecutive_x)
            consecutive_x = 0
    max_consecutive_x = max(max_consecutive_x, consecutive_x)
    max_consecutive_x += k
    max_consecutive_x = min(max_consecutive_x, n)
    return max_consecutive_x

s = input()
k = int(input())
print(solve(s, k))

=======
Suggestion 4

def main():
    S = input()
    K = int(input())
    max = 0
    count = 0
    for i in range(len(S)):
        if S[i] == "X":
            count += 1
        else:
            if max < count:
                max = count
            count = 0
    if max < count:
        max = count
    if K == 0:
        print(max)
        return
    if max + K > len(S):
        print(len(S))
        return
    print(max + K)

=======
Suggestion 5

def main():
    s = input()
    k = int(input())

    # s = "XX...X.X.X."
    # k = 2

    # s = "XXXX"
    # k = 200000

    s = s.replace(".", "0")
    s = s.replace("X", "1")
    s = s.replace("0", "X")
    s = s.replace("1", "0")

    s = "0" + s + "0"

    count = 0
    max_count = 0

    for i in range(1, len(s)):
        if s[i] == "0":
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 0

    if max_count < count:
        max_count = count

    print(max_count + k)

=======
Suggestion 6

def main():
    s = input()
    k = int(input())
    n = len(s)
    ans = 0
    for i in range(n - 1):
        if s[i] == s[i + 1] == 'X':
            ans += 1
    ans += min(ans + k, n - 1)
    print(ans)

=======
Suggestion 7

def main():
    S = input()
    K = int(input())
    N = len(S)
    if K == 0:
        ans = 0
        count = 0
        for s in S:
            if s == "X":
                count += 1
            else:
                ans = max(ans, count)
                count = 0
        ans = max(ans, count)
        print(ans)
        return
    ans = 0
    count = 0
    for s in S:
        if s == "X":
            count += 1
        else:
            ans = max(ans, count)
            count = 0
    ans = max(ans, count)
    if K >= 2:
        count = 0
        for s in S:
            if s == "X":
                count += 1
            else:
                ans = max(ans, count + 1)
                count = 0
        ans = max(ans, count + 1)
    print(ans)

=======
Suggestion 8

def main():
    s = input()
    k = int(input())
    s = s.replace('X', 'XX')
    s = s.replace('.', 'X')
    s = s.replace('X', '.')
    s = s.replace('..', '.')
    s = s.replace('X', 'XX')
    print(min(len(s), len(s) + k))

=======
Suggestion 9

def main():
    s = input()
    k = int(input())
    s0 = s.replace('.', ' ')
    s1 = s0.split()
    s2 = list(map(len, s1))
    l = len(s2)
    if l == 1:
        if s[0] == '.':
            if k == 0:
                print(0)
            else:
                print(min(k, s2[0]))
        else:
            print(s2[0])
    else:
        if s[0] == '.':
            if k == 0:
                print(s2[0])
            else:
                print(min(k, s2[0]))
        else:
            ans = s2[0]
            for i in range(1, l):
                ans = max(ans, s2[i - 1] + s2[i])
            if s[-1] == '.':
                ans = max(ans, s2[-1])
            else:
                ans = max(ans, s2[-1] + min(k, s2[-1]))
            print(ans)

=======
Suggestion 10

def main():
    s = input()
    k = int(input())
    # print(s, k)
    # print(len(s))
    # print(s.find('X'))
    # print(s.rfind('X'))
    # print(s[0:1])
    # print(s[1:2])
    # print(s[2:3])
    # print(s[3:4])
    # print(s[4:5])
    # print(s[5:6])
    # print(s[6:7])
    # print(s[7:8])
    # print(s[8:9])
    # print(s[9:10])
    # print(s[10:11])
    # print(s[11:12])
    # print(s[12:13])
    # print(s[13:14])
    # print(s[14:15])
    # print(s[15:16])
    # print(s[16:17])
    # print(s[17:18])
    # print(s[18:19])
    # print(s[19:20])
    # print(s[20:21])
    # print(s[21:22])
    # print(s[22:23])
    # print(s[23:24])
    # print(s[24:25])
    # print(s[25:26])
    # print(s[26:27])
    # print(s[27:28])
    # print(s[28:29])
    # print(s[29:30])
    # print(s[30:31])
    # print(s[31:32])
    # print(s[32:33])
    # print(s[33:34])
    # print(s[34:35])
    # print(s[35:36])
    # print(s[36:37])
    # print(s[37:38])
    # print(s[38:39])
    # print(s[39:40])
    # print(s[40:41])
    # print(s[41:42])
    # print(s[42:43])
    # print(s[43:44])
    # print(s[44:45])
    # print(s[45:46])
    # print(s[46:47])
    # print(s[47:48])
    # print(s[48:49])
    # print(s[49:50])
    # print(s[50:
