Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print("AC x " + str(s.count("AC")))
    print("WA x " + str(s.count("WA")))
    print("TLE x " + str(s.count("TLE")))
    print("RE x " + str(s.count("RE")))

=======
Suggestion 2

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print('AC x ' + str(s.count('AC')))
    print('WA x ' + str(s.count('WA')))
    print('TLE x ' + str(s.count('TLE')))
    print('RE x ' + str(s.count('RE')))

=======
Suggestion 3

def main():
    N = int(input())
    S = [input() for i in range(N)]
    print("AC x " + str(S.count("AC")))
    print("WA x " + str(S.count("WA")))
    print("TLE x " + str(S.count("TLE")))
    print("RE x " + str(S.count("RE")))

=======
Suggestion 4

def main():
    n = int(input())
    s = [input() for i in range(n)]
    print("AC x", s.count("AC"))
    print("WA x", s.count("WA"))
    print("TLE x", s.count("TLE"))
    print("RE x", s.count("RE"))

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    print("AC x " + str(S.count("AC")))
    print("WA x " + str(S.count("WA")))
    print("TLE x " + str(S.count("TLE")))
    print("RE x " + str(S.count("RE")))

=======
Suggestion 6

def main():
    n = int(input())
    verdicts = []
    for i in range(n):
        verdicts.append(input())
    print("AC x " + str(verdicts.count("AC")))
    print("WA x " + str(verdicts.count("WA")))
    print("TLE x " + str(verdicts.count("TLE")))
    print("RE x " + str(verdicts.count("RE")))

=======
Suggestion 7

def main():
    n = int(input())
    verdicts = [input() for _ in range(n)]
    verdicts_dict = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
    for verdict in verdicts:
        verdicts_dict[verdict] += 1
    print('AC x', verdicts_dict['AC'])
    print('WA x', verdicts_dict['WA'])
    print('TLE x', verdicts_dict['TLE'])
    print('RE x', verdicts_dict['RE'])

=======
Suggestion 8

def problem173_b():
    n = int(input())
    s_list = []
    for i in range(n):
        s_list.append(input())
    print("AC x " + str(s_list.count("AC")))
    print("WA x " + str(s_list.count("WA")))
    print("TLE x " + str(s_list.count("TLE")))
    print("RE x " + str(s_list.count("RE")))

=======
Suggestion 9

def main():
    n = int(input())
    verdict = ['AC', 'WA', 'TLE', 'RE']
    verdict_count = [0] * 4
    for i in range(n):
        verdict_count[verdict.index(input())] += 1
    for i in range(4):
        print(verdict[i], 'x', verdict_count[i])

=======
Suggestion 10

def main():
    # Your code here!
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print("AC x " + str(S.count("AC")))
    print("WA x " + str(S.count("WA")))
    print("TLE x " + str(S.count("TLE")))
    print("RE x " + str(S.count("RE")))
