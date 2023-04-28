Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    count = 0
    for i in range(3, n + 1):
        if '7' in str(i) and '5' in str(i) and '3' in str(i):
            count += 1
    print(count)

=======
Suggestion 2

def isShichiGoSan(num):
    numStr = str(num)
    if "7" in numStr and "5" in numStr and "3" in numStr:
        return True
    else:
        return False

=======
Suggestion 3

def shichi_go_san(num):
    if num < 357:
        return 0
    else:
        if '7' in str(num) and '5' in str(num) and '3' in str(num):
            return 1 + shichi_go_san(num-1)
        else:
            return shichi_go_san(num-1)

print(shichi_go_san(int(input())))

=======
Suggestion 4

def isSGS(n):
    n = str(n)
    if '7' in n and '5' in n and '3' in n:
        return True
    else:
        return False

n = int(input())
count = 0
for i in range(1, n+1):
    if isSGS(i):
        count += 1
print(count)

=======
Suggestion 5

def isShichiGoSan(number):
    number = str(number)
    if '7' in number and '5' in number and '3' in number:
        return True
    return False

=======
Suggestion 6

def main():
    n = int(input())
    cnt = 0
    for i in range(3, len(str(n))+1):
        for j in range(3**i):
            s = ''
            for k in range(i):
                if j%(3**(k+1))//3**k == 0:
                    s += '3'
                elif j%(3**(k+1))//3**k == 1:
                    s += '5'
                else:
                    s += '7'
            if int(s) <= n and len(set(s)) == 3:
                cnt += 1
    print(cnt)

=======
Suggestion 7

def isShichiGoSan(n):
    if n<357:
        return False
    else:
        n=str(n)
        if "7" in n and "5" in n and "3" in n:
            return True
        else:
            return False

=======
Suggestion 8

def is753num(n):
    if n % 10 == 7 or n % 10 == 5 or n % 10 == 3:
        return True
    else:
        return False

=======
Suggestion 9

def is_sgs(x):
    x_str = str(x)
    return "7" in x_str and "5" in x_str and "3" in x_str

n = int(input())

sgs = 0
queue = [3, 5, 7]

while queue:
    x = queue.pop()
    if x > n:
        continue
    if is_sgs(x):
        sgs += 1
    queue.append(x * 10 + 3)
    queue.append(x * 10 + 5)
    queue.append(x * 10 + 7)

print(sgs)

=======
Suggestion 10

def check753(num):
    if num > 1000000000:
        return False
    if num < 100:
        return False
    if num < 1000:
        if num == 375 or num == 537 or num == 573:
            return True
        else:
            return False
    if num < 10000:
        if num == 3573 or num == 3753 or num == 5373 or num == 5733:
            return True
        else:
            return False
    if num < 100000:
        if num == 35753 or num == 35773 or num == 37573 or num == 53753 or num == 53773 or num == 57353:
            return True
        else:
            return False
    if num < 1000000:
        if num == 357373 or num == 537573 or num == 537773 or num == 573373:
            return True
        else:
            return False
    if num < 10000000:
        if num == 3575373 or num == 5375373 or num == 5375733 or num == 5377733 or num == 5735373:
            return True
        else:
            return False
    if num < 100000000:
        if num == 35753773 or num == 53753773 or num == 53757373 or num == 57353773:
            return True
        else:
            return False
    if num < 1000000000:
        if num == 357537773 or num == 537537773 or num == 573537773:
            return True
        else:
            return False
