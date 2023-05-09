Synthesizing 10/10 solutions

=======
Suggestion 1

def lunlun(n):
    if n < 10:
        return n
    last = n % 10
    if last == 0:
        return lunlun(n // 10 - 1) * 10 + 9
    if last == 9:
        return lunlun(n // 10) * 10 + 8
    return lunlun(n // 10) * 10 + last - 1

K = int(input())
for i in range(K):
    print(lunlun(i+1))

=======
Suggestion 2

def solve(k):
    lunlun = [1,2,3,4,5,6,7,8,9]
    for _ in range(k-1):
        x = lunlun.pop(0)
        if x%10 != 0:
            lunlun.append(10*x + x%10 - 1)
        lunlun.append(10*x + x%10)
        if x%10 != 9:
            lunlun.append(10*x + x%10 + 1)
    return lunlun[0]

k = int(input())
print(solve(k))

=======
Suggestion 3

def main():
    k = int(input())
    lunlun = [i for i in range(1,10)]
    while len(lunlun) < k:
        new_lunlun = []
        for l in lunlun:
            last_digit = l % 10
            if last_digit == 0:
                new_lunlun.append(l * 10 + last_digit)
                new_lunlun.append(l * 10 + last_digit + 1)
            elif last_digit == 9:
                new_lunlun.append(l * 10 + last_digit - 1)
                new_lunlun.append(l * 10 + last_digit)
            else:
                new_lunlun.append(l * 10 + last_digit - 1)
                new_lunlun.append(l * 10 + last_digit)
                new_lunlun.append(l * 10 + last_digit + 1)
        lunlun = new_lunlun
    print(lunlun[k - 1])

=======
Suggestion 4

def main():
    k = int(input())
    lunlun = [1,2,3,4,5,6,7,8,9]
    for i in range(1, k):
        x = lunlun[i]
        if x % 10 != 0:
            lunlun.append(10 * x + x % 10 - 1)
        lunlun.append(10 * x + x % 10)
        if x % 10 != 9:
            lunlun.append(10 * x + x % 10 + 1)
    print(lunlun[k-1])

=======
Suggestion 5

def main():
    k = int(input())
    lunlun_list = [i for i in range(1,10)]
    if k <= 9:
        print(lunlun_list[k-1])
    else:
        k -= 9
        while k > 0:
            new_lunlun_list = []
            for lunlun in lunlun_list:
                last_digit = lunlun % 10
                if last_digit == 0:
                    new_lunlun_list.append(lunlun * 10)
                    new_lunlun_list.append(lunlun * 10 + 1)
                elif last_digit == 9:
                    new_lunlun_list.append(lunlun * 10 + last_digit - 1)
                    new_lunlun_list.append(lunlun * 10 + last_digit)
                else:
                    new_lunlun_list.append(lunlun * 10 + last_digit - 1)
                    new_lunlun_list.append(lunlun * 10 + last_digit)
                    new_lunlun_list.append(lunlun * 10 + last_digit + 1)
            lunlun_list = new_lunlun_list
            k -= len(lunlun_list)
        print(lunlun_list[k-1])

=======
Suggestion 6

def lunlun(k):
    lunlun_list = [1,2,3,4,5,6,7,8,9]
    for i in range(1, 11):
        for j in range(-1, 2):
            if lunlun_list[i] % 10 + j >= 0 and lunlun_list[i] % 10 + j <= 9:
                lunlun_list.append(lunlun_list[i] * 10 + lunlun_list[i] % 10 + j)
    print(lunlun_list[k-1])

k = int(input())
lunlun(k)

=======
Suggestion 7

def lunlun_number():
    K = int(input())
    q = []
    for i in range(1,10):
        q.append(i)
    for i in range(K):
        x = q.pop(0)
        if x % 10 != 0:
            q.append(10*x + x%10 - 1)
        q.append(10*x + x%10)
        if x % 10 != 9:
            q.append(10*x + x%10 + 1)
    print(x)

=======
Suggestion 8

def lunlun(k):
    if k <= 9:
        return k
    k -= 9
    digits = 2
    while True:
        if k <= 9 * 10 ** (digits - 1):
            break
        k -= 9 * 10 ** (digits - 1)
        digits += 1
    for i in range(10 ** (digits - 1), 10 ** digits):
        if k <= get_count(i):
            return i
        k -= get_count(i)

=======
Suggestion 9

def lunlun(n):
    if n < 10:
        return n
    else:
        n = str(n)
        a = int(n[-1])
        if a == 9:
            return lunlun(int(n[:-1]))*10 + a
        else:
            return lunlun(int(n[:-1]))*10 + a - 1

K = int(input())
ans = 0
for i in range(K):
    ans = lunlun(ans+1)
print(ans)

=======
Suggestion 10

def lunlun(n):
    if n < 10:
        return n
    else:
        keta = len(str(n))
        if keta == 2:
            return n
        elif keta == 3:
            n1 = int(str(n)[0])
            n2 = int(str(n)[1])
            n3 = int(str(n)[2])
            if n2 == 0:
                return n1*10 + n2
            elif abs(n2-n3) <= 1:
                return n
            else:
                return (n1+1)*10 + n1
        elif keta == 4:
            n1 = int(str(n)[0])
            n2 = int(str(n)[1])
            n3 = int(str(n)[2])
            n4 = int(str(n)[3])
            if n2 == 0:
                return n1*100 + n2*10 + n3
            elif abs(n2-n3) <= 1:
                return n
            elif abs(n3-n4) <= 1:
                return (n1+1)*100 + n1*10 + n1
            else:
                return (n1+1)*100 + n1*10 + n1
        elif keta == 5:
            n1 = int(str(n)[0])
            n2 = int(str(n)[1])
            n3 = int(str(n)[2])
            n4 = int(str(n)[3])
            n5 = int(str(n)[4])
            if n2 == 0:
                return n1*1000 + n2*100 + n3*10 + n4
            elif abs(n2-n3) <= 1:
                return n
            elif abs(n3-n4) <= 1:
                return (n1+1)*1000 + n1*100 + n1*10 + n1
            elif abs(n4-n5) <= 1:
                return (n1+1)*1000 + n1*100 + n1*10 + n1
            else:
                return (n1+1)*1000 + n1*100 + n1*10 + n1
        else:
            n1 = int(str(n)[0])
            n2 = int(str(n)[1])
            n3 = int(str(n)[2])
