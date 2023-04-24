Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if s <= "2019/04/30":
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 2

def main():
    S = input()
    if S <= "2019/04/30":
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 3

def main():
    date = input()
    if date <= "2019/04/30":
        print("Heisei")
    else:
        print("TBD")

=======
Suggestion 4

def main():
    S = input()
    S = S.split('/')
    if int(S[0]) == 2019 and int(S[1]) <= 4 and int(S[2]) <= 30:
        print('Heisei')
    else:
        print('TBD')

=======
Suggestion 5

def main():
    s = input()
    s_list = s.split('/')
    if int(s_list[1]) <= 4:
        print('Heisei')
    else:
        print('TBD')
