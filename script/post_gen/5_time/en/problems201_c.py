Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    print(s.count('o')*100 + s.count('?')*100 - s.count('x')*100 + s.count('o')*10 + s.count('?')*10 - s.count('x')*10 + s.count('o') + s.count('?') - s.count('x'))

=======
Suggestion 2

def main():
    S = input()
    count = 0
    for i in range(10000):
        i = str(i).zfill(4)
        flag = True
        for j in range(10):
            if S[j] == "o" and str(j) not in i:
                flag = False
            if S[j] == "x" and str(j) in i:
                flag = False
        if flag:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    S = input()
    count = 0
    for i in range(10000):
        pin = str(i).zfill(4)
        flag = True
        for j in range(10):
            if S[j] == 'o' and str(j) not in pin:
                flag = False
            if S[j] == 'x' and str(j) in pin:
                flag = False
        if flag:
            count += 1
    print(count)

=======
Suggestion 4

def check_pin(pin, s):
    for i in range(10):
        if s[i] == 'o':
            if str(i) not in pin:
                return False
        elif s[i] == 'x':
            if str(i) in pin:
                return False
    return True

=======
Suggestion 5

def main():
    S = input()
    count = 0
    for i in range(10000):
        i = str(i).zfill(4)
        for j in range(10):
            if S[j] == 'o' and str(j) not in i:
                break
            if S[j] == 'x' and str(j) in i:
                break
        else:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    s = input()
    o = s.count("o")
    x = s.count("x")
    q = s.count("?")
    if o >= 5:
        print(0)
    elif o == 4:
        print(24)
    elif o == 3:
        print(36)
    elif o == 2:
        print(14 + 12 * q)
    elif o == 1:
        print(1 + 4 * q + 6 * q * (q - 1))
    elif o == 0:
        print(q * (q - 1) * (q - 2) * (q - 3))
    else:
        print(0)

=======
Suggestion 7

def main():
    s = input()
    print(s.count('o') * 100 + s.count('?') * 100 - s.count('o') * 10)

=======
Suggestion 8

def main():
    s = input()
    count = 0
    for i in range(10000):
        pin = str(i).zfill(4)
        isPin = True
        for j in range(10):
            if s[j] == 'o' and str(j) not in pin:
                isPin = False
            if s[j] == 'x' and str(j) in pin:
                isPin = False
        if isPin:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    s = input()
    count = 0
    for i in range(10000):
        if len(str(i)) < 4:
            i = str(i).zfill(4)
        else:
            i = str(i)
        flag = True
        for j in range(len(s)):
            if s[j] == 'o' and str(j) not in i:
                flag = False
                break
            if s[j] == 'x' and str(j) in i:
                flag = False
                break
        if flag:
            count += 1
    print(count)

=======
Suggestion 10

def main():
    s = input()
    count = 0
    for i in range(10000):
        if len(str(i)) < 4:
            if s.count("o") > 0:
                count = 0
                break
            else:
                count += 1
        else:
            if s.count(str(i)) == 4:
                count += 1
    print(count)
