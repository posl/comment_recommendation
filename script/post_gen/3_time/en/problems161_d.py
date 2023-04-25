Synthesizing 10/10 solutions

=======
Suggestion 1

def is_lunlun(n):
    n = str(n)
    for i in range(len(n)-1):
        if abs(int(n[i]) - int(n[i+1])) > 1:
            return False
    return True

=======
Suggestion 2

def is_lunlun(n):
    s = str(n)
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) > 1:
            return False
    return True

=======
Suggestion 3

def isLunlun(n):
    s = str(n)
    for i in range(len(s) - 1):
        if abs(ord(s[i]) - ord(s[i + 1])) > 1:
            return False
    return True

=======
Suggestion 4

def lunlun(n):
    if n < 10:
        return True
    else:
        n = str(n)
        for i in range(len(n)-1):
            if abs(int(n[i])-int(n[i+1])) > 1:
                return False
        return True

=======
Suggestion 5

def solve():
    K = int(input())
    lunlun = [1,2,3,4,5,6,7,8,9]
    for i in range(K-1):
        num = lunlun.pop(0)
        last_num = num % 10
        if last_num == 0:
            lunlun.append(num*10)
            lunlun.append(num*10+1)
        elif last_num == 9:
            lunlun.append(num*10+8)
            lunlun.append(num*10+9)
        else:
            lunlun.append(num*10+last_num-1)
            lunlun.append(num*10+last_num)
            lunlun.append(num*10+last_num+1)
    print(lunlun[0])

=======
Suggestion 6

def isLunlun(num):
    if len(num) < 2:
        return True
    if abs(int(num[0]) - int(num[1])) > 1:
        return False
    return isLunlun(num[1:])

=======
Suggestion 7

def lunlun(n):
    if n < 10:
        return n
    else:
        num = str(n)
        for i in range(len(num)-1):
            if abs(int(num[i]) - int(num[i+1])) > 1:
                return 0
        return n

=======
Suggestion 8

def solve(K):
    lunlun = [1,2,3,4,5,6,7,8,9]
    for i in range(9):
        if len(lunlun) >= K:
            return lunlun[K-1]
        lunlun.append(lunlun[i]*10 + lunlun[i]%10 - 1)
        lunlun.append(lunlun[i]*10 + lunlun[i]%10)
        lunlun.append(lunlun[i]*10 + lunlun[i]%10 + 1)
        lunlun = [x for x in lunlun if 0 < x <= 10**9]

=======
Suggestion 9

def lunlun(n):
    if n < 10:
        return n
    else:
        return lunlun(n // 10) * 10 + n % 10

=======
Suggestion 10

def lunlun(k):
    if k <= 9:
        return k
    n = 9
    a = [i for i in range(1, 10)]
    while n < k:
        x = a.pop(0)
        for i in range(-1, 2):
            y = x % 10 + i
            if y >= 0 and y <= 9:
                a.append(x * 10 + y)
        n += 1
    return a[0]

k = int(input())
print(lunlun(k))
