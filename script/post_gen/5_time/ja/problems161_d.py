Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def check(n):
    if n < 10:
        return True
    else:
        s = str(n)
        for i in range(1, len(s)):
            if abs(int(s[i]) - int(s[i-1])) > 1:
                return False
    return True

k = int(input())
cnt = 0
n = 1
while True:
    if check(n):
        cnt += 1
        if cnt == k:
            print(n)
            break
    n += 1

=======
Suggestion 2

def isLunlun(n):
    s = str(n)
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) > 1:
            return False
    return True

=======
Suggestion 3

def is_lunlun(n):
    s = str(n)
    for i in range(len(s)-1):
        if abs(int(s[i]) - int(s[i+1])) > 1:
            return False
    return True

K = int(input())
cnt = 0
i = 0
while True:
    i += 1
    if is_lunlun(i):
        cnt += 1
    if cnt == K:
        print(i)
        break

=======
Suggestion 4

def l(x):
    if x == 0:
        return 0
    elif x < 10:
        return 1
    else:
        return 1 + l(x // 10)

=======
Suggestion 5

def check(x):
    s = str(x)
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) > 1:
            return False
    return True

K = int(input())
cnt = 0
i = 0
while True:
    i += 1
    if check(i):
        cnt += 1
        if cnt == K:
            print(i)
            break

=======
Suggestion 6

def main():
    k = int(input())
    lunlun = [1,2,3,4,5,6,7,8,9]
    for i in range(1, k):
        x = lunlun[i]
        if x % 10 == 0:
            lunlun.append(x * 10)
            lunlun.append(x * 10 + 1)
        elif x % 10 == 9:
            lunlun.append(x * 10 + 8)
            lunlun.append(x * 10 + 9)
        else:
            lunlun.append(x * 10 + x % 10 - 1)
            lunlun.append(x * 10 + x % 10)
            lunlun.append(x * 10 + x % 10 + 1)
    print(lunlun[k - 1])

=======
Suggestion 7

def is_lunlun(n):
    s = str(n)
    for i in range(len(s)-1):
        if abs(int(s[i]) - int(s[i+1])) > 1:
            return False
    return True

K = int(input())
cnt = 0
for i in range(10**20):
    if is_lunlun(i):
        cnt += 1
        if cnt == K:
            print(i)
            break

=======
Suggestion 8

def main():
    k = int(input())
    if k <= 9:
        print(k)
        return
    k -= 9
    cnt = 9
    for i in range(10, 10**9):
        if k <= cnt * 2:
            k -= 1
            s = str(i)
            print(s[k])
            return
        else:
            k -= cnt * 2
            cnt *= 10

=======
Suggestion 9

def main():
    k = int(input())
    count = 0
    i = 0
    while count < k:
        i += 1
        if i < 10:
            count += 1
        else:
            s = str(i)
            flag = True
            for j in range(len(s) - 1):
                if abs(int(s[j]) - int(s[j + 1])) > 1:
                    flag = False
                    break
            if flag:
                count += 1
    print(i)
