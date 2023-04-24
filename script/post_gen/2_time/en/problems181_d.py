Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    if len(S) == 1:
        if int(S) % 8 == 0:
            print('Yes')
        else:
            print('No')
    elif len(S) == 2:
        if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
            print('Yes')
        else:
            print('No')
    else:
        S = list(S)
        S.sort()
        for i in range(100, 1000, 8):
            if str(i).count('0') == 2:
                continue
            if str(i)[0] in S:
                if str(i)[1] in S:
                    if str(i)[2] in S:
                        print('Yes')
                        return
        print('No')

=======
Suggestion 2

def main():
    S = input()
    if '0' in S or '1' in S or '2' in S:
        print('Yes')
        return
    if len(S) == 1:
        print('No')
        return
    if '3' in S:
        if '4' in S:
            print('Yes')
            return
        if '6' in S:
            print('Yes')
            return
        if '8' in S:
            print('Yes')
            return
        if len(S) == 2:
            print('No')
            return
        if '5' in S:
            if '7' in S:
                print('Yes')
                return
            if '9' in S:
                print('Yes')
                return
            print('No')
            return
        if '7' in S:
            if '9' in S:
                print('Yes')
                return
            print('No')
            return
        print('No')
        return
    if '4' in S:
        if '6' in S:
            print('Yes')
            return
        if '8' in S:
            print('Yes')
            return
        if len(S) == 2:
            print('No')
            return
        if '5' in S:
            if '7' in S:
                print('Yes')
                return
            if '9' in S:
                print('Yes')
                return
            print('No')
            return
        if '7' in S:
            if '9' in S:
                print('Yes')
                return
            print('No')
            return
        print('No')
        return
    if '5' in S:
        if '7' in S:
            print('Yes')
            return
        if '9' in S:
            print('Yes')
            return
        print('No')
        return
    if '6' in S:
        if '8' in S:
            print('Yes')
            return
        if len(S) == 2:
            print('No')
            return
        if '7' in S:
            if '9' in S:
                print('Yes')
                return
            print('No')
            return
        print('No')
        return
    if '7' in S:
        if '9'

=======
Suggestion 3

def main():
    S = input()
    if '0' in S or '1' in S or '2' in S:
        print('Yes')
    elif len(S) == 2:
        if int(S) % 8 == 0:
            print('Yes')
        else:
            print('No')
    else:
        for i in range(112, 1000, 8):
            if str(i).count('0') == 0 and str(i).count('1') == 0 and str(i).count('2') == 0:
                if str(i).count('3') <= S.count('3') and str(i).count('4') <= S.count('4') and str(i).count('5') <= S.count('5') and str(i).count('6') <= S.count('6') and str(i).count('7') <= S.count('7') and str(i).count('8') <= S.count('8') and str(i).count('9') <= S.count('9'):
                    print('Yes')
                    return
        print('No')

=======
Suggestion 4

def main():
    S = input()
    if '0' in S or '1' in S or '2' in S:
        print('Yes')
    elif '3' in S and '4' in S and '5' in S:
        print('Yes')
    elif '4' in S and '5' in S and '6' in S:
        print('Yes')
    elif '5' in S and '6' in S and '7' in S:
        print('Yes')
    elif '6' in S and '7' in S and '8' in S:
        print('Yes')
    elif '7' in S and '8' in S and '9' in S:
        print('Yes')
    elif '3' in S and '6' in S and '9' in S:
        print('Yes')
    elif '3' in S and '5' in S and '8' in S:
        print('Yes')
    elif '4' in S and '6' in S and '9' in S:
        print('Yes')
    elif '4' in S and '7' in S and '9' in S:
        print('Yes')
    elif '5' in S and '7' in S and '9' in S:
        print('Yes')
    elif '2' in S and '5' in S and '8' in S:
        print('Yes')
    elif '2' in S and '6' in S and '9' in S:
        print('Yes')
    elif '2' in S and '4' in S and '7' in S:
        print('Yes')
    elif '2' in S and '3' in S and '6' in S:
        print('Yes')
    elif '1' in S and '4' in S and '7' in S:
        print('Yes')
    elif '1' in S and '3' in S and '6' in S:
        print('Yes')
    elif '1' in S and '5' in S and '8' in S:
        print('Yes')
    elif '1' in S and '2' in S and '5' in S:
        print('Yes')
    elif '0' in S and '3' in S and '6' in

=======
Suggestion 5

def main():
    s = input()
    if s == '8':
        print('Yes')
        return
    if len(s) == 1:
        print('No')
        return
    if len(s) == 2:
        if int(s) % 8 == 0:
            print('Yes')
            return
        if int(s[::-1]) % 8 == 0:
            print('Yes')
            return
        print('No')
        return
    s = sorted(s)
    for i in range(104, 1000, 8):
        if sorted(str(i)) == s:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 6

def main():
    S = input()
    for i in range(1000):
        if str(i).zfill(3)[-1] != '0' and str(i).zfill(3)[-1] != '8':
            continue
        S1 = S
        for j in str(i).zfill(3):
            if j in S1:
                S1 = S1.replace(j, '', 1)
            else:
                break
        else:
            print('Yes')
            return
    print('No')

=======
Suggestion 7

def permute(s):
    if len(s) == 1:
        return [s]
    else:
        perms = []
        for i in range(len(s)):
            for p in permute(s[:i] + s[i+1:]):
                perms.append(s[i] + p)
        return perms

=======
Suggestion 8

def main():
    S = list(input())
    for i in range(1, 10):
        if str(i) in S:
            print("Yes")
            return
    for i in range(1, 10):
        for j in range(1, 10):
            if str(i) in S and str(j) in S:
                if (i*10 + j) % 8 == 0:
                    print("Yes")
                    return
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if str(i) in S and str(j) in S and str(k) in S:
                    if (i*100 + j*10 + k) % 8 == 0:
                        print("Yes")
                        return
    print("No")
    return

=======
Suggestion 9

def main():
    S = input()
    S = list(S)
    S = list(map(int, S))
    S.sort()
    if 0 in S:
        print('Yes')
        return
    for i in range(len(S)-2):
        for j in range(i+1, len(S)-1):
            for k in range(j+1, len(S)):
                if (S[i]*100 + S[j]*10 + S[k]) % 8 == 0:
                    print('Yes')
                    return
    print('No')
    return

=======
Suggestion 10

def main():
    S = input()
    
    if S.count("8") > 0:
        print("Yes")
        exit()
    
    for i in range(1, len(S)):
        for j in range(0, len(S)-i):
            if (int(S[j:j+i+1]) % 8) == 0:
                print("Yes")
                exit()
    print("No")
