Synthesizing 10/10 solutions

=======
Suggestion 1

def isLunLun(x):
    if x < 10:
        return True
    else:
        x = str(x)
        for i in range(1, len(x)):
            if abs(int(x[i]) - int(x[i-1])) > 1:
                return False
        return True

=======
Suggestion 2

def isLunLunNumber(n):
    s = str(n)
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) > 1:
            return False
    return True

=======
Suggestion 3

def main():
    K = int(input())
    anslist = []
    for i in range(1, 10):
        anslist.append(i)
    while len(anslist) < K:
        tmp = []
        for i in anslist:
            lastnum = i % 10
            if lastnum == 0:
                tmp.append(i * 10)
                tmp.append(i * 10 + 1)
            elif lastnum == 9:
                tmp.append(i * 10 + 8)
                tmp.append(i * 10 + 9)
            else:
                tmp.append(i * 10 + lastnum - 1)
                tmp.append(i * 10 + lastnum)
                tmp.append(i * 10 + lastnum + 1)
        anslist = tmp
    anslist.sort()
    print(anslist[K - 1])

=======
Suggestion 4

def isLunlun(n):
    n = str(n)
    for i in range(len(n) - 1):
        if abs(int(n[i]) - int(n[i + 1])) > 1:
            return False
    return True

=======
Suggestion 5

def isLLSK(n):
    s = str(n)
    for i in range(1, len(s)):
        if abs(int(s[i]) - int(s[i - 1])) > 1:
            return False
    return True

=======
Suggestion 6

def isLuckyNum(num):
    numStr = str(num)
    for i in range(len(numStr)-1):
        if abs(int(numStr[i])-int(numStr[i+1])) > 1:
            return False
    return True

=======
Suggestion 7

def search(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 3
    elif n==4:
        return 4
    elif n==5:
        return 5
    elif n==6:
        return 6
    elif n==7:
        return 7
    elif n==8:
        return 8
    elif n==9:
        return 9
    else:
        for i in range(1,10):
            if n>=i*10**(len(str(i)))+i:
                continue
            else:
                return i*10**(len(str(i)))+search(n-i*10**(len(str(i))))


n=int(input())
print(search(n-1))

=======
Suggestion 8

def isLunLun(x):
    s = str(x)
    for i in range(len(s)-1):
        if abs(int(s[i]) - int(s[i+1])) > 1:
            return False
    return True

=======
Suggestion 9

def check(num):
    num = str(num)
    length = len(num)
    for i in range(length):
        if i == length-1:
            return True
        if abs(int(num[i])-int(num[i+1])) > 1:
            return False

=======
Suggestion 10

def is_repdigit(n):
    s = str(n)
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) > 1:
            return False
    return True

k = int(input())

cnt = 0
n = 0
while True:
    n += 1
    if is_repdigit(n):
        cnt += 1
    if cnt == k:
        break
print(n)
