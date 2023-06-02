Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    S = input()
    l = len(S)
    ans = 100000
    for i in range(l-1):
        if S[i] == '0':
            continue
        else:
            ans = min(ans, i+l-1-i+int(S[i:]))
    print(ans)

=======
Suggestion 3

def solve():
    s = input()
    n = len(s)
    ans = n
    for i in range(n-1):
        if s[i] == '1':
            ans = min(ans, i+n-1-i)
    print(ans)

solve()

=======
Suggestion 4

def main():
    s = input()
    if len(s) == 1:
        print(0)
        return
    if len(s) == 2:
        print(1)
        return
    if len(s) == 3:
        print(2)
        return
    if len(s) == 4:
        print(3)
        return
    if len(s) == 5:
        print(4)
        return
    if len(s) == 6:
        print(5)
        return
    if len(s) == 7:
        print(6)
        return
    if len(s) == 8:
        print(7)
        return
    if len(s) == 9:
        print(8)
        return
    if len(s) == 10:
        print(9)
        return
    if len(s) == 11:
        print(10)
        return
    if len(s) == 12:
        print(11)
        return
    if len(s) == 13:
        print(12)
        return
    if len(s) == 14:
        print(13)
        return
    if len(s) == 15:
        print(14)
        return
    if len(s) == 16:
        print(15)
        return
    if len(s) == 17:
        print(16)
        return
    if len(s) == 18:
        print(17)
        return
    if len(s) == 19:
        print(18)
        return
    if len(s) == 20:
        print(19)
        return
    if len(s) == 21:
        print(20)
        return
    if len(s) == 22:
        print(21)
        return
    if len(s) == 23:
        print(22)
        return
    if len(s) == 24:
        print(23)
        return
    if len(s) == 25:
        print(24)
        return
    if len(s) == 26:
        print(25)
        return
    if len(s) == 27:
        print(26)
        return
    if len(s) == 28:
        print(27)
        return
    if len(s) == 29:
        print(28)
        return

=======
Suggestion 5

def main():
    s = input()
    n = len(s)
    ans = n
    for i in range(n):
        if s[i] != '0':
            ans = min(ans, i + n - s[::-1].index(s[i]))
    print(ans)

=======
Suggestion 6

def solve(S):
    ans = 1000000000000000000000000000
    for i in range(len(S)):
        for j in range(i, len(S)):
            if S[i] != '0' or j == i:
                ans = min(ans, i + len(S) - j + S.count('0', i, j+1))
    return ans

=======
Suggestion 7

def main():
    S = int(input())
    print(S)
    return

=======
Suggestion 8

def main():
    s = input()
    s_len = len(s)
    # print(s_len)
    # print(s)
    # print(s[0])
    # print(s[s_len-1])
    # print(type(s))
    # print(type(s[0]))
    # print(type(s[s_len-1]))
    # print("s[0] = ", s[0])
    # print("s[s_len-1] = ", s[s_len-1])

    # print("s[0] = ", int(s[0]))
    # print("s[s_len-1] = ", int(s[s_len-1]))

    # print("s[0] = ", type(int(s[0])))
    # print("s[s_len-1] = ", type(int(s[s_len-1])))

    # print("s[0] = ", int(s[0]) * 10)
    # print("s[s_len-1] = ", int(s[s_len-1]) * 10)

    # print("s[0] = ", type(int(s[0]) * 10))
    # print("s[s_len-1] = ", type(int(s[s_len-1]) * 10))

    # print("s[0] = ", int(s[0]) * 100)
    # print("s[s_len-1] = ", int(s[s_len-1]) * 100)

    # print("s[0] = ", type(int(s[0]) * 100))
    # print("s[s_len-1] = ", type(int(s[s_len-1]) * 100))

    # print("s[0] = ", int(s[0]) * 1000)
    # print("s[s_len-1] = ", int(s[s_len-1]) * 1000)

    # print("s[0] = ", type(int(s[0]) * 1000))
    # print("s[s_len-1] = ", type(int(s[s_len-1]) * 1000))

    # print("s[0] = ", int(s[0]) * 10000)
    # print("s[s_len-1] = ", int(s[s_len-1]) * 10000)

    # print("s[0] = ", type(int(s[0]) * 10000))
    # print("s

=======
Suggestion 9

def main():
    S = int(input())
    print(S)
    print(type(S))
    ans = 0
    while S > 0:
        #print(S)
        if S % 100 == 0:
            S /= 100
        else:
            S -= 1
        ans += 1
    print(ans)
