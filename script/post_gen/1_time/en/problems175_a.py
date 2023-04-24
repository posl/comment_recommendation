Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    count = 0
    max_count = 0
    for i in range(len(S)):
        if S[i] == 'R':
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)

=======
Suggestion 2

def main():
    S = input()
    if S == 'SSS':
        print(0)
    elif S == 'RRS' or S == 'SRR' or S == 'RSR':
        print(1)
    else:
        print(2)

=======
Suggestion 3

def main():
    S = input()
    cnt = 0
    max_cnt = 0
    for s in S:
        if s == 'R':
            cnt += 1
        else:
            if cnt > max_cnt:
                max_cnt = cnt
            cnt = 0
    if cnt > max_cnt:
        max_cnt = cnt
    print(max_cnt)

=======
Suggestion 4

def main():
    s = input()
    count = 0
    maxCount = 0
    for i in range(len(s)):
        if s[i] == 'R':
            count += 1
        else:
            if count > maxCount:
                maxCount = count
            count = 0
    if count > maxCount:
        maxCount = count
    print(maxCount)

=======
Suggestion 5

def main():
    S = input()
    if S == "RRS":
        print(2)
    elif S == "SSS":
        print(0)
    else:
        print(1)

main()

=======
Suggestion 6

def main():
    S = input()
    max_count = 0
    count = 0
    for i in range(0, 3):
        if S[i] == 'R':
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    print(max_count)

=======
Suggestion 7

def main():
    S = input()
    maxRainyDays = 0
    currentRainyDays = 0
    for i in range(3):
        if S[i] == 'R':
            currentRainyDays += 1
            if currentRainyDays > maxRainyDays:
                maxRainyDays = currentRainyDays
        else:
            currentRainyDays = 0
    print(maxRainyDays)

=======
Suggestion 8

def main():
    s = input()
    n = 0
    m = 0
    for i in range(len(s)):
        if s[i] == "R":
            n += 1
            m = max(n, m)
        else:
            n = 0
    print(m)

=======
Suggestion 9

def maxRainyDays():
    S = input()
    count = 0
    maxCount = 0
    for i in range(len(S)):
        if S[i] == 'R':
            count += 1
        else:
            count = 0
        if count > maxCount:
            maxCount = count
    return maxCount

print(maxRainyDays())

=======
Suggestion 10

def main():
    s = input()
    #print(s)
    max = 0
    count = 0
    for i in range(3):
        if s[i] == "R":
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    print(max)

main()
