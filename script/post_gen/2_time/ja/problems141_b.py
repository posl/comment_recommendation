Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[::2].count('R') + s[::2].count('U') + s[::2].count('D') == len(s[::2]) and s[1::2].count('L') + s[1::2].count('U') + s[1::2].count('D') == len(s[1::2]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    s = input()
    if s[0::2].count('R') + s[0::2].count('U') + s[0::2].count('D') == len(s[0::2]) and s[1::2].count('L') + s[1::2].count('U') + s[1::2].count('D') == len(s[1::2]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    S = input()
    if S[::2].count("R") + S[::2].count("U") + S[::2].count("D") == len(S[::2]) and S[1::2].count("L") + S[1::2].count("U") + S[1::2].count("D") == len(S[1::2]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S = input()
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] == 'L':
                print('No')
                return
        else:
            if S[i] == 'R':
                print('No')
                return
    print('Yes')

=======
Suggestion 5

def main():
    S = input()
    if S[0] == "R" or S[0] == "U" or S[0] == "D":
        if S[1] == "L" or S[1] == "U" or S[1] == "D":
            if S[2] == "R" or S[2] == "U" or S[2] == "D":
                if S[3] == "L" or S[3] == "U" or S[3] == "D":
                    if S[4] == "R" or S[4] == "U" or S[4] == "D":
                        if S[5] == "L" or S[5] == "U" or S[5] == "D":
                            if S[6] == "R" or S[6] == "U" or S[6] == "D":
                                if S[7] == "L" or S[7] == "U" or S[7] == "D":
                                    if S[8] == "R" or S[8] == "U" or S[8] == "D":
                                        if S[9] == "L" or S[9] == "U" or S[9] == "D":
                                            if S[10] == "R" or S[10] == "U" or S[10] == "D":
                                                if S[11] == "L" or S[11] == "U" or S[11] == "D":
                                                    if S[12] == "R" or S[12] == "U" or S[12] == "D":
                                                        if S[13] == "L" or S[13] == "U" or S[13] == "D":
                                                            if S[14] == "R" or S[14] == "U" or S[14] == "D":
                                                                if S[15] == "L" or S[15] == "U" or S[15] == "D":
                                                                    if S[16] == "R" or S[16] == "U" or S[16] == "D":
                                                                        if S[17] == "L" or S[17] == "

=======
Suggestion 6

def main():
    s = input()
    if s[0::2].count("R") == 0 and s[1::2].count("L") == 0:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 7

def main():
    S = input()
    if (S[::2].count("U") + S[::2].count("D") == len(S[::2])) and (S[1::2].count("L") + S[1::2].count("R") == len(S[1::2])):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    S = input()
    if S[::2] == 'RUDL' and S[1::2] == 'LUDR':
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    S = input()
    print("Yes" if S[::2].count("R") + S[1::2].count("L") == len(S[::2]) else "No")

=======
Suggestion 10

def main():
    # 1行目
    s = input()
    # 2行目
    # n = int(input())
    # 3行目
    # a, b = map(int, input().split())
    # 4行目
    # a = list(map(int, input().split()))
    # 5行目
    # a = [input() for i in range(n)]
    # 6行目
    # a = [list(input()) for i in range(n)]
    # 7行目
    # a = [list(map(int, input().split())) for i in range(n)]
    # 8行目
    # a = [[int(input()) for i in range(n)] for j in range(n)]
    # 9行目
    # a = [[input() for i in range(n)] for j in range(n)]

    # 1行目
    # print(s)
    # 2行目
    # print(n)
    # 3行目
    # print(a, b)
    # 4行目
    # print(a)
    # 5行目
    # print(a)
    # 6行目
    # print(a)
    # 7行目
    # print(a)
    # 8行目
    # print(a)
    # 9行目
    # print(a)

    # 1行目
    # print(s)
    # 2行目
    # print(n)
    # 3行目
    # print(a, b)
    # 4行目
    # print(*a)
    # 5行目
    # print(*a, sep="

")
    # 6行目
    # print(*a, sep="

")
    # 7行目
    # print(*a, sep="

")
    # 8行目
    # print(*a, sep="

")
    # 9行目
    # print(*a, sep="

")

    # 1行目
    # print(s)
    # 2行目
    # print(n)
    # 3行目
    # print(a, b)
    # 4行目
    # print(*a, sep="")
    # 5行目
    # print(*a, sep
