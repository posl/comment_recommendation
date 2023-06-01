Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    num = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(num):
        s = input()
        if s == "AC":
            a += 1
        elif s == "WA":
            b += 1
        elif s == "TLE":
            c += 1
        elif s == "RE":
            d += 1
    print("AC x " + str(a))
    print("WA x " + str(b))
    print("TLE x " + str(c))
    print("RE x " + str(d))

=======
Suggestion 2

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
Suggestion 3

def main():
    N = int(input())
    ac = 0
    wa = 0
    tle = 0
    re = 0
    for i in range(N):
        S = input()
        if S == "AC":
            ac += 1
        elif S == "WA":
            wa += 1
        elif S == "TLE":
            tle += 1
        else:
            re += 1
    print("AC x " + str(ac))
    print("WA x " + str(wa))
    print("TLE x " + str(tle))
    print("RE x " + str(re))

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for i in range(N)]

    ac = wa = tle = re = 0
    for i in range(N):
        if S[i] == "AC":
            ac += 1
        elif S[i] == "WA":
            wa += 1
        elif S[i] == "TLE":
            tle += 1
        elif S[i] == "RE":
            re += 1

    print("AC x " + str(ac))
    print("WA x " + str(wa))
    print("TLE x " + str(tle))
    print("RE x " + str(re))

=======
Suggestion 5

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print("AC x " + str(s.count("AC")))
    print("WA x " + str(s.count("WA")))
    print("TLE x " + str(s.count("TLE")))
    print("RE x " + str(s.count("RE")))

main()

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print('AC x', s.count('AC'))
    print('WA x', s.count('WA'))
    print('TLE x', s.count('TLE'))
    print('RE x', s.count('RE'))
main()

=======
Suggestion 7

def main():
    n = int(input())
    s = [input() for i in range(n)]
    print('AC x', s.count('AC'))
    print('WA x', s.count('WA'))
    print('TLE x', s.count('TLE'))
    print('RE x', s.count('RE'))

=======
Suggestion 8

def count(s):
    count = [0,0,0,0]
    for i in s:
        if i == "AC":
            count[0] += 1
        elif i == "WA":
            count[1] += 1
        elif i == "TLE":
            count[2] += 1
        elif i == "RE":
            count[3] += 1
    return count

n = int(input())
s = []
for i in range(n):
    s.append(input())
count = count(s)
print("AC x",count[0])
print("WA x",count[1])
print("TLE x",count[2])
print("RE x",count[3])

=======
Suggestion 9

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print("AC x {}".format(s.count("AC")))
    print("WA x {}".format(s.count("WA")))
    print("TLE x {}".format(s.count("TLE")))
    print("RE x {}".format(s.count("RE")))

=======
Suggestion 10

def main():
    n = int(input())
    s = [input() for i in range(n)]
    print("AC x", s.count("AC"))
    print("WA x", s.count("WA"))
    print("TLE x", s.count("TLE"))
    print("RE x", s.count("RE"))
