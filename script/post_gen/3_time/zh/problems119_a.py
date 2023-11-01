Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    date = input()
    year, month, day = date.split("/")
    if year <= '2019' and month <= '04' and day <= '30':

=======
Suggestion 2

def main():
    s = input()
    year, month, day = map(int, s.split("/"))
    if year < 2019:
        print("Heisei")
    elif year

=======
Suggestion 3

def main():
    s = input()
    year, month, day = s.split("/")
    if int(year) < 2019:
        print("Heisei")
    elif int(month

=======
Suggestion 4

def main():
    s = input()
    y = int(s[0:4])
    m = int(s[5:7])
    d = int(s[8:])
    if y < 2019:
        print("Heisei")

=======
Suggestion 5

def problem119_a():
    S = input()
    S = S.split('/')
    if int(S[0]) < 2019:
        print("Heisei")
    elif int(S[0]) == 2

=======
Suggestion 6

def main():
    S = input()
    S = S.split("/")
    if int(S[0]) < 2019:
        print("Heisei")
    elif int(S[1]) < 4:

=======
Suggestion 7

def main():
    S = input().split("/")
    if int(S[0]) < 2019:
        print("Heisei")
    elif int(S[0]) == 2019 and int(S[1])

=======
Suggestion 8

def main():
    s = input()
    y, m, d = s.split('/')
    if int(y) < 2019:
        print('Heisei')
    elif int(m) < 4:

=======
Suggestion 9

def main():
    #输入
    S=input()
    #处理
    #输出
    if S<="2019/04/30":
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 10

def main():
    s = input()
    s = s.split("/")
    if int(s[1]) <= 4:
        print("Heisei")
    else:
        print("TBD")
