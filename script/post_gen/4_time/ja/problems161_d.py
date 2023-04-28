Synthesizing 10/10 solutions

=======
Suggestion 1

def is_lunlun(n):
    s = str(n)
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) > 1:
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

k = int(input())
lunlun = [i for i in range(1, 10)]
while len(lunlun) < k:
    n = lunlun.pop(0)
    if n % 10 > 0:
        lunlun.append(n*10 + n%10 - 1)
    lunlun.append(n*10 + n%10)
    if n % 10 < 9:
        lunlun.append(n*10 + n%10 + 1)
print(lunlun[0])

=======
Suggestion 3

def is_lunlun(n):
    s = str(n)
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) > 1:
            return False
    return True

k = int(input())
lunlun = []
for i in range(1,10):
    lunlun.append(i)
while len(lunlun) < k:
    n = lunlun.pop(0)
    for i in range(max(0,n%10-1),min(10,n%10+2)):
        lunlun.append(n*10+i)
print(lunlun[0])

=======
Suggestion 4

def check(x):
    s = str(x)
    for i in range(1,len(s)):
        if abs(int(s[i-1])-int(s[i])) > 1:
            return False
    return True

K = int(input())
cnt = 0
x = 0
while cnt < K:
    x += 1
    if check(x):
        cnt += 1

print(x)

=======
Suggestion 5

def is_rurun(x):
    if x < 10:
        return True
    s = str(x)
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) > 1:
            return False
    return True

k = int(input())
cnt = 0
i = 1
while True:
    if is_rurun(i):
        cnt += 1
        if cnt == k:
            print(i)
            break
    i += 1

=======
Suggestion 6

def is_rururun(n):
    if n < 10:
        return True
    n_str = str(n)
    for i in range(1, len(n_str)):
        if abs(int(n_str[i]) - int(n_str[i-1])) > 1:
            return False
    return True

k = int(input())
cnt = 0
i = 0
while cnt < k:
    i += 1
    if is_rururun(i):
        cnt += 1
print(i)

=======
Suggestion 7

def is_rurun(x):
    if x < 10:
        return True
    x = str(x)
    for i in range(1,len(x)):
        if abs(int(x[i-1])-int(x[i])) > 1:
            return False
    return True

=======
Suggestion 8

def lunlun(n):
    if n == 0:
        return [0]
    else:
        result = []
        for i in lunlun(n-1):
            if i%10 != 0:
                result.append(i*10 + i%10 - 1)
            result.append(i*10 + i%10)
            if i%10 != 9:
                result.append(i*10 + i%10 + 1)
        return result

k = int(input())
print(sorted(lunlun(10))[k-1])

=======
Suggestion 9

def isLunlun(n):
    if n < 10:
        return True
    if n % 10 == 0:
        return False
    if n < 100:
        return True
    if n % 100 == 0:
        return False
    if n < 1000:
        return True
    if n % 1000 == 0:
        return False
    if n < 10000:
        return True
    if n % 10000 == 0:
        return False
    if n < 100000:
        return True
    if n % 100000 == 0:
        return False
    if n < 1000000:
        return True
    if n % 1000000 == 0:
        return False
    if n < 10000000:
        return True
    if n % 10000000 == 0:
        return False
    if n < 100000000:
        return True
    if n % 100000000 == 0:
        return False
    if n < 1000000000:
        return True
    if n % 1000000000 == 0:
        return False
    if n < 10000000000:
        return True
    if n % 10000000000 == 0:
        return False
    if n < 100000000000:
        return True
    if n % 100000000000 == 0:
        return False
    if n < 1000000000000:
        return True
    if n % 1000000000000 == 0:
        return False
    if n < 10000000000000:
        return True
    if n % 10000000000000 == 0:
        return False
    if n < 100000000000000:
        return True
    if n % 100000000000000 == 0:
        return False
    if n < 1000000000000000:
        return True
    if n % 1000000000000000 == 0:
        return False
    if n < 10000000000000000:
        return True
    if n % 10000000000000000 == 0:
        return False
    if n < 100000000000000000:

=======
Suggestion 10

def main():
    K = int(input())
    #print("K:{}".format(K))
    #print("type K:{}".format(type(K)))
    #print("K-1:{}".format(K-1))
    #print("type K-1:{}".format(type(K-1)))

    #print("K-1:{}".format(K-1))
    #print("type K-1:{}".format(type(K-1)))
    #print("K-1%9:{}".format(K-1%9))
    #print("type K-1%9:{}".format(type(K-1%9)))
    #print("K-1//9:{}".format(K-1//9))
    #print("type K-1//9:{}".format(type(K-1//9)))

    #print("K-1%9+1:{}".format(K-1%9+1))
    #print("type K-1%9+1:{}".format(type(K-1%9+1)))
    #print("K-1//9+1:{}".format(K-1//9+1))
    #print("type K-1//9+1:{}".format(type(K-1//9+1)))

    #print("K-1%9-1:{}".format(K-1%9-1))
    #print("type K-1%9-1:{}".format(type(K-1%9-1)))
    #print("K-1//9:{}".format(K-1//9))
    #print("type K-1//9:{}".format(type(K-1//9)))

    #print("K-1%9:{}".format(K-1%9))
    #print("type K-1%9:{}".format(type(K-1%9)))
    #print("K-1//9-1:{}".format(K-1//9-1))
    #print("type K-1//9-1:{}".format(type(K-1//9-1)))

    #print("K-1%9+1:{}".format(K-1%9+1))
    #print("type K-1%9+1:{}".format(type(K-1%9+1)))
    #print("K-1//9+1:{}".format(K-1//9+1))
    #print("type K
