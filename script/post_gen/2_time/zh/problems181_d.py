Synthesizing 10/10 solutions

=======
Suggestion 1

def judge(num):
    if num%8==0:
        return True
    else:
        return False

=======
Suggestion 2

def judge(s):
    for i in range(1,10):
        if s.count(str(i))>0:
            if i%8==0:
                return True
    return False

s=input()

=======
Suggestion 3

def judge(s):
    if len(s) == 1:
        if s == "8":
            return True
        else:
            return False
    elif len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            return True
        else:
            return False
    else:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in range(112, 1000, 8):
            t = str(i)
            dt = {}
            for j in t:
                if j in dt:
                    dt[j] += 1
                else:
                    dt[j] = 1
            if dt == d:
                return True
        return False

s = input()

=======
Suggestion 4

def main():
    S = input()
    S = list(S)
    #print(S)
    for i in range(len(S)):
        S[i] = int(S[i])
    #print(S)
    S.sort()
    #print(S)
    if len(S) == 1:
        if S[0] == 8:
            print("Yes")
        else:
            print("No")
        return
    if len(S) == 2:
        if (S[0]*10 + S[1]) % 8 == 0 or (S[1]*10 + S[0]) % 8 == 0:
            print("Yes")
        else:
            print("No")
        return
    if len(S) == 3:
        if (S[0]*100 + S[1]*10 + S[2]) % 8 == 0 or (S[0]*100 + S[2]*10 + S[1]) % 8 == 0 or (S[1]*100 + S[0]*10 + S[2]) % 8 == 0 or (S[1]*100 + S[2]*10 + S[0]) % 8 == 0 or (S[2]*100 + S[0]*10 + S[1]) % 8 == 0 or (S[2]*100 + S[1]*10 + S[0]) % 8 == 0:
            print("Yes")
        else:
            print("No")
        return
    if len(S) == 4:
        if (S[0]*1000 + S[1]*100 + S[2]*10 + S[3]) % 8 == 0 or (S[0]*1000 + S[1]*100 + S[3]*10 + S[2]) % 8 == 0 or (S[0]*1000 + S[2]*100 + S[1]*10 + S[3]) % 8 == 0 or (S[0]*1000 + S[2]*100 + S[3]*10 + S[1]) % 8 == 0 or (S[0]*1000 + S[3]*100 + S[1]*10 + S[2]) % 8 == 0 or (S[0]*1000 + S[3]*100 + S[

=======
Suggestion 5

def main():
    S = input()
    if len(S) == 1:
        if S == '8':
            print("是")
        else:
            print("否")
        return
    if len(S) == 2:
        if int(S)%8 == 0 or int(S[1]+S[0])%8 == 0:
            print("是")
        else:
            print("否")
        return
    if len(S) == 3:
        if int(S)%8 == 0 or int(S[2]+S[0]+S[1])%8 == 0 or int(S[1]+S[2]+S[0])%8 == 0 or int(S[2]+S[1]+S[0])%8 == 0 or int(S[1]+S[0]+S[2])%8 == 0:
            print("是")
        else:
            print("否")
        return
    if len(S) == 4:
        if int(S)%8 == 0 or int(S[3]+S[0]+S[1]+S[2])%8 == 0 or int(S[2]+S[3]+S[0]+S[1])%8 == 0 or int(S[1]+S[2]+S[3]+S[0])%8 == 0 or int(S[0]+S[1]+S[2]+S[3])%8 == 0 or int(S[3]+S[2]+S[1]+S[0])%8 == 0 or int(S[2]+S[1]+S[0]+S[3])%8 == 0 or int(S[1]+S[0]+S[3]+S[2])%8 == 0:
            print("是")
        else:
            print("否")
        return
    if len(S) == 5:
        if int(S)%8 == 0 or int(S[4]+S[0]+S[1]+S[2]+S[3])%8 == 0 or int(S[3]+S[4]+S[0]+S[1]+S[2])%8 == 0 or int(S[2]+S[3]+S[4]+S[0]+S[1])%8 == 0 or int(S[1

=======
Suggestion 6

def main():
    s = input()
    #s = "1234"
    #s = "1333"
    #s = "8"
    #s = "1234567890"
    #s = "1234567890123456789012345678901234567890123456789012345678901234567890"
    #s = "1234567890123456789012345678901234567890123456789012345678901234567890"
    #s = "1234567890123456789012345678901234567890123456789012345678901234567890"
    #s = "1234567890123456789012345678901234567890123456789012345678901234567890"
    #s = "1234567890123456789012345678901234567890123456789012345678901234567890"
    #s = "1234567890123456789012345678901234567890123456789012345678901234567890"
    #s = "1234567890123456789012345678901234567890123456789012345678901234567890"
    #s = "1234567890123456789012345678901234567890123456789012345678901234567890"
    #s = "1234567890123456789012345678901234567890123456789012345678901234567890"
    #s = "1234567890123456789012345678901234567890123456789012345678901234567890"
    #s = "123456789012345678901234567890123456789012345678901234567890123456789"

    #print(s)
    s = list(s)
    #print(s)
    #print(len(s))
    #print(s[0])
    #print(s[1])
    #print(s[2])
    #print(s[3])
    #print(s[4])
    #print(s[5])
    #print(s[6])
    #print(s[7])
    #print(s[8])
    #print(s[9])
    #print(s[10])
    #print(s[11])
    #print(s[12])
    #print(s[13])
    #print(s[14])
    #print(s

=======
Suggestion 7

def main():
    s = input()
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    for i in range(1000, 2000, 8):
        dd = {}
        for c in str(i):
            if c in dd:
                dd[c] += 1
            else:
                dd[c] = 1
        for c in dd:
            if not c in d or dd[c] > d[c]:
                break
        else:
            print("是")
            break
    else:
        print("否")

=======
Suggestion 8

def is_8(n):
    for i in range(1,10):
        if n.count(str(i)) == 0:
            continue
        if n.count(str(i)) > 3:
            return False
    return True

=======
Suggestion 9

def is_8(x):
    x = str(x)
    if len(x) == 1:
        if x == '8':
            return True
        else:
            return False
    elif len(x) == 2:
        if int(x) % 8 == 0:
            return True
        elif int(x[1] + x[0]) % 8 == 0:
            return True
        else:
            return False
    else:
        for i in range(len(x)):
            for j in range(len(x)):
                for k in range(len(x)):
                    if i != j and j != k and k != i:
                        if int(x[i] + x[j] + x[k]) % 8 == 0:
                            return True
        return False

s = input()

=======
Suggestion 10

def solve():
    s = input()
    if len(s) <= 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print('是')
        else:
            print('否')
        return

    cnt = [0] * 10
    for c in s:
        cnt[int(c)] += 1

    for i in range(112, 1000, 8):
        t = [0] * 10
        t[i % 10] += 1
        t[(i // 10) % 10] += 1
        t[i // 100] += 1
        if all(t[j] <= cnt[j] for j in range(10)):
            print('是')
            return
    print('否')

solve()
