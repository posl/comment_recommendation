Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if 'RR' in S:
        print(2)
    elif 'R' in S:
        print(1)
    else:
        print(0)

=======
Suggestion 2

def main():
    S = input()
    count = 0
    max_count = 0
    for s in S:
        if s == "R":
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    print(max_count)

=======
Suggestion 3

def main():
    S = input()
    if S == 'RRR':
        print(3)
    elif S[0] == 'R' or S[1] == 'R' or S[2] == 'R':
        print(1)
    else:
        print(0)

=======
Suggestion 4

def main():
    S = input()
    count = 0
    max_count = 0
    for i in range(len(S)):
        if S[i] == 'R':
            count += 1
        else:
            max_count = max(count, max_count)
            count = 0
    max_count = max(count, max_count)
    print(max_count)

=======
Suggestion 5

def main():
    S = input()
    cnt = 0
    max = 0
    for i in range(3):
        if S[i] == 'R':
            cnt += 1
            if cnt > max:
                max = cnt
        else:
            cnt = 0
    print(max)

=======
Suggestion 6

def main():
    S = input()
    count = 0
    max_count = 0
    for i in range(3):
        if S[i] == 'R':
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 0
    if max_count < count:
        max_count = count
    print(max_count)

=======
Suggestion 7

def main():
    S = input()
    ans = 0
    count = 0
    for i in S:
        if i == "R":
            count += 1
        else:
            if count > ans:
                ans = count
            count = 0
    if count > ans:
        ans = count
    print(ans)

=======
Suggestion 8

def main():
    S = input()
    rain = 0
    max_rain = 0
    for i in range(3):
        if S[i] == "R":
            rain += 1
        else:
            rain = 0
        if max_rain < rain:
            max_rain = rain
    print(max_rain)

=======
Suggestion 9

def main():
    S = input()
    #print(S)
    #print(len(S))
    max = 0
    count = 0
    for i in range(len(S)):
        if S[i] == "R":
            count += 1
            if max < count:
                max = count
        else:
            count = 0
    print(max)

=======
Suggestion 10

def main():
    S = input()
    print(max(len(x) for x in S.split('S')))
