Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    # print(s)
    if 'R' in s:
        print(1)
    else:
        print(0)

=======
Suggestion 2

def main():
    s = input()
    print(s.count("R"))

=======
Suggestion 3

def main():
    S = input()
    R = S.count('R')
    print(R)

=======
Suggestion 4

def main():
    S = input()
    print(S.count("R"))

=======
Suggestion 5

def main():
    s = input()
    if s == 'RRR':
        print(3)
    elif s == 'RRS' or s == 'SRR':
        print(2)
    elif s == 'SSS':
        print(0)
    else:
        print(1)

=======
Suggestion 6

def main():
    s = input()
    count = 0
    max_count = 0
    for i in range(len(s)):
        if s[i] == 'R':
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 0
    print(max_count)

=======
Suggestion 7

def main():
    s = input()
    a = s.count("R")
    print(a)

=======
Suggestion 8

def main():
    S = input()
    #print(S)
    rain = 0
    max_rain = 0
    for i in range(len(S)):
        #print(S[i])
        if S[i] == 'S':
            rain = 0
        elif S[i] == 'R':
            rain += 1
        if max_rain < rain:
            max_rain = rain
    print(max_rain)

=======
Suggestion 9

def main():
    S = input()
    S = S.replace("S","0")
    S = S.replace("R","1")
    print(S.count("1"))

=======
Suggestion 10

def main():
    weather = input()
    count = 0
    max = 0
    for i in range(len(weather)):
        if weather[i] == 'R':
            count += 1
        else:
            count = 0
        if count > max:
            max = count
    print(max)
