Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    n = len(s)
    cnt = [0] * 2019
    cnt[0] = 1
    t = 0
    p = 1
    for i in range(n - 1, -1, -1):
        t = (t + int(s[i]) * p) % 2019
        p = p * 10 % 2019
        cnt[t] += 1
    ans = 0
    for i in range(2019):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)

=======
Suggestion 2

def main():
    # 读取输入
    S = input()

    # 累积和
    A = [0] * (len(S) + 1)
    for i in range(len(S)):
        A[i + 1] = A[i] + int(S[i])

    # 计算每个余数的出现次数
    count = [0] * 2019
    for a in A:
        count[a % 2019] += 1

    # 计算答案
    ans = 0
    for c in count:
        ans += c * (c - 1) // 2
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    s = list(map(int, s))
    s.reverse()
    print(s)
    ans = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if (s[i] + s[j] * 10) % 2019 == 0:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    #print(S)
    length = len(S)
    #print(length)
    #print(S[0:1])
    #print(S[0:2])
    #print(S[0:3])
    #print(S[0:4])
    #print(S[0:5])
    #print(S[0:6])
    #print(S[0:7])
    #print(S[0:8])
    #print(S[0:9])
    #print(S[0:10])
    #print(S[0:11])
    #print(S[0:12])
    #print(S[0:13])
    #print(S[0:14])
    #print(S[0:15])
    #print(S[0:16])
    #print(S[0:17])
    #print(S[0:18])
    #print(S[0:19])
    #print(S[0:20])
    #print(S[0:21])
    #print(S[0:22])
    #print(S[0:23])
    #print(S[0:24])
    #print(S[0:25])
    #print(S[0:26])
    #print(S[0:27])
    #print(S[0:28])
    #print(S[0:29])
    #print(S[0:30])
    #print(S[0:31])
    #print(S[0:32])
    #print(S[0:33])
    #print(S[0:34])
    #print(S[0:35])
    #print(S[0:36])
    #print(S[0:37])
    #print(S[0:38])
    #print(S[0:39])
    #print(S[0:40])
    #print(S[0:41])
    #print(S[0:42])
    #print(S[0:43])
    #print(S[0:44])
    #print(S[0:45])
    #print(S[0:46])
    #print(S[0:47])
    #print(S[0:48])
    #print(S[0:49])
    #print(S[0:50])
    #print(S[0:51])
    #print(S[0:52])
    #print(S[0:53])

=======
Suggestion 5

def main():
    S = input()
    N = len(S)
    cnt = [0] * 2019
    cnt[0] = 1
    t = 0
    for i in range(N):
        t = (t + int(S[N - 1 - i]) * pow(10, i, 2019)) % 2019
        cnt[t] += 1
    ans = 0
    for c in cnt:
        ans += c * (c - 1) // 2
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    n = len(s)
    mod = 2019
    ans = 0
    cnt = [0] * mod
    cnt[0] = 1
    t = 0
    for i in range(n):
        t = (t + int(s[n - 1 - i]) * pow(10, i, mod)) % mod
        ans += cnt[t]
        cnt[t] += 1
    print(ans)

=======
Suggestion 7

def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if int(s[i:j + 1]) % 2019 == 0:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    S = input()
    n = len(S)
    # 余数为key，出现次数为value
    mod = {i: 0 for i in range(2019)}
    mod[0] = 1
    # 从右往左，从1位数到n位数
    # 1位数
    x = 0
    for i in range(n):
        x += int(S[n-1-i]) * pow(10, i, 2019)
        x %= 2019
        mod[x] += 1
    # 2位数到n位数
    ans = 0
    for i in mod:
        # 从出现两次的余数中任选两个
        ans += mod[i] * (mod[i]-1) // 2
    print(ans)

=======
Suggestion 9

def main():
    S = input()
    count = 0
    for i in range(len(S)):
        for j in range(i, len(S)):
            if int(S[i:j+1]) % 2019 == 0:
                count += 1
    print(count)

=======
Suggestion 10

def main():
    s = input()
    # 10进制数转换为2019进制数
    # 2019进制数中，个位数是0-8，十位数是0-18，百位数是0-18，千位数是0-18
    # 2019进制数中，个位数是0-8，十位数是0-9，百位数是0-9，千位数是0-1
    # 2019进制数中，个位数是0-8，十位数是0-9，百位数是0-9，千位数是0-1
    # 2019进制数中，个位数是0-8，十位数是0-9，百位数是0-9，千位数是0-1
    # 2019进制数中，个位数是0-8，十位数是0-9，百位数是0-9，千位数是0-1
    # 2019进制数中，个位数是0-8，十位数是0-9，百位数是0-9，千位数是0-1
    # 2019进制数中，个位数是0-8，十位数是0-9，百位数是0-9，千位数是0-1
    # 2019进制数中，个位数是0-8，十位数是0-9，百位数是0-9，千位数是0-1
    # 2019进制数中，个位数是0-8，十位数是0-9，百位数是0-9，千位数是0-1
    # 2019进制数中，个位数是0-8，十位数是0-9，百位数是0-9，千位数是0-1

    # 2019进制数中，个位数是0-8，十位数是0-9，百位数是0-9，千
