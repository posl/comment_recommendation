Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 2

def main():
    s = input()
    if s[0] == s[1] == s[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 3

def main():
    c1, c2, c3 = input().split()
    if c1 == c2 and c2 == c3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 4

def main():
    s = input()
    if s[0] == s[1] == s[2]:
        print('Won')
    else:
        print('Lost')

=======
Suggestion 5

def main():
    a = input()
    if a[0] == a[1] and a[1] == a[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 6

def main():
    c1, c2, c3 = input().split()
    if c1 == c2 == c3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 7

def main():
    C_1, C_2, C_3 = input().rstrip().split()
    if C_1 == C_2 == C_3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 8

def main():
    #input
    C1,C2,C3 = input()

    #compute
    if C1 == C2 and C2 == C3:
        print("Won")
    else:
        print("Lost")

    #output

=======
Suggestion 9

def main():
    # スペース区切りの整数の入力
    C = input()
    # 文字列をリストに格納
    C_list = list(C)
    # 全て同じ文字ならWon
    if C_list[0] == C_list[1] == C_list[2]:
        print('Won')
    else:
        print('Lost')
