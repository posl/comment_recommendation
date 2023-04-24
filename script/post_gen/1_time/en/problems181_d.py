Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if len(S) == 1:
        if int(S) % 8 == 0:
            print("Yes")
        else:
            print("No")
    elif len(S) == 2:
        if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
            print("Yes")
        else:
            print("No")
    else:
        s = [0] * 10
        for i in S:
            s[int(i)] += 1
        for i in range(100, 1000, 8):
            t = s[:]
            for j in str(i):
                t[int(j)] -= 1
                if t[int(j)] < 0:
                    break
            else:
                print("Yes")
                break
        else:
            print("No")

=======
Suggestion 2

def check(S):
    if len(S) == 1:
        if int(S) % 8 == 0:
            return True
        else:
            return False
    elif len(S) == 2:
        if int(S) % 8 == 0:
            return True
        elif int(S[1] + S[0]) % 8 == 0:
            return True
        else:
            return False
    else:
        for i in range(104, 1000, 8):
            if all(S.count(str(j)) >= str(i).count(str(j)) for j in range(10)):
                return True
        return False

=======
Suggestion 3

def main():
    S = input()
    if '0' in S or '1' in S or '2' in S:
        print('Yes')
    elif len(S) == 2:
        if int(S) % 8 == 0:
            print('Yes')
        elif int(S[::-1]) % 8 == 0:
            print('Yes')
        else:
            print('No')
    else:
        for i in range(112, 1000, 8):
            if str(i).count('0') == 0 and str(i).count('1') == 0 and str(i).count('2') == 0:
                if str(i)[0] in S and str(i)[1] in S and str(i)[2] in S:
                    print('Yes')
                    exit()
        print('No')

=======
Suggestion 4

def main():
    S = input()
    if "0" in S:
        print("Yes")
        return
    if "8" in S:
        print("Yes")
        return
    if len(S) < 2:
        print("No")
        return
    for i in range(10, 100, 8):
        if str(i)[0] in S and str(i)[1] in S:
            print("Yes")
            return
    if len(S) < 3:
        print("No")
        return
    for i in range(100, 1000, 8):
        if str(i)[0] in S and str(i)[1] in S and str(i)[2] in S:
            print("Yes")
            return
    print("No")

=======
Suggestion 5

def main():
    S = input()
    for i in range(0, len(S)):
        for j in range(i, len(S)):
            for k in range(j, len(S)):
                if int(S[i] + S[j] + S[k]) % 8 == 0:
                    print('Yes')
                    return
    print('No')

=======
Suggestion 6

def main():
    s = input()
    if '0' in s:
        print('Yes')
        return
    if '1' in s and '2' in s:
        print('Yes')
        return
    if '3' in s and '4' in s:
        print('Yes')
        return
    if '5' in s and '6' in s:
        print('Yes')
        return
    if '7' in s and '8' in s:
        print('Yes')
        return
    if '9' in s and '0' in s:
        print('Yes')
        return
    print('No')

=======
Suggestion 7

def main():
    S = input()
    if S.count('0') > 0:
        print('Yes')
        return
    if len(S) < 2:
        print('No')
        return
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            if int(S[i] + S[j]) % 8 == 0:
                print('Yes')
                return
    print('No')

=======
Suggestion 8

def main():
    s = input()
    if '0' in s or '1' in s or '2' in s:
        print('Yes')
    elif len(s) >= 2 and ('0' in s[1:] or '1' in s[1:] or '2' in s[1:]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    S = input()
    if "8" in S:
        print("Yes")
        return
    for i in range(len(S)):
        for j in range(len(S)):
            if i == j:
                continue
            if int(S[i]+S[j])%8 == 0:
                print("Yes")
                return
    print("No")

=======
Suggestion 10

def main():
    S = input()
    S = sorted(S)
    S = S[::-1]
    #print(S)
    for i in range(0, len(S)):
        for j in range(i+1, len(S)):
            for k in range(j+1, len(S)):
                s = int(S[i] + S[j] + S[k])
                if s % 8 == 0:
                    print('Yes')
                    return
    print('No')
