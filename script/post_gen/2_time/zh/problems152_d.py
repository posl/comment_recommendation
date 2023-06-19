Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        if i % 10 == 0:
            continue
        for j in range(1, n+1):
            if j % 10 == 0:
                continue
            if str(i)[-1] == str(j)[0] and str(i)[0] == str(j)[-1]:
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    cnt = 0
    for i in range(1, n + 1):
        s = str(i)
        if s[-1] == s[0]:
            cnt += 1
    for i in range(1, n + 1):
        s = str(i)
        if s[-1] != s[0]:
            continue
        for j in range(1, n + 1):
            s = str(j)
            if s[-1] != s[0]:
                continue
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i % 10 == j // 10 and i // 10 == j % 10:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if i < 10:
            count += 1
        else:
            if i % 10 == i // 10000 and (i // 10) % 10 == (i // 1000) % 10:
                count += 1
    print(count)

=======
Suggestion 5

def getNums(n):
    nums = 0
    for i in range(1, n+1):
        if i < 10:
            nums += 1
        elif i < 100:
            if i % 11 == 0:
                nums += 1
        elif i < 1000:
            if i % 11 == 0:
                nums += 2
        elif i < 10000:
            if i % 11 == 0:
                nums += 3
        elif i < 100000:
            if i % 11 == 0:
                nums += 4
        elif i < 1000000:
            if i % 11 == 0:
                nums += 5
        elif i < 10000000:
            if i % 11 == 0:
                nums += 6
        elif i < 100000000:
            if i % 11 == 0:
                nums += 7
        elif i < 1000000000:
            if i % 11 == 0:
                nums += 8
        elif i < 10000000000:
            if i % 11 == 0:
                nums += 9
        elif i < 100000000000:
            if i % 11 == 0:
                nums += 10
        elif i < 1000000000000:
            if i % 11 == 0:
                nums += 11
        elif i < 10000000000000:
            if i % 11 == 0:
                nums += 12
        elif i < 100000000000000:
            if i % 11 == 0:
                nums += 13
        elif i < 1000000000000000:
            if i % 11 == 0:
                nums += 14
        elif i < 10000000000000000:
            if i % 11 == 0:
                nums += 15
        elif i < 100000000000000000:
            if i % 11 == 0:
                nums += 16
        elif i < 1000000000000000000:
            if i % 11 == 0:
                nums += 17
        elif i < 10000000000000000000:
            if i % 11 == 0

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            k = str(i)
            l = str(j)
            if k[-1] == l[0] and k[0] == l[-1]:
                ans += 1
    print(ans)

=======
Suggestion 7

def pair(a,b):
    if a%10==b//100:
        return True
    else:
        return False

=======
Suggestion 8

def get_num(n):
    count = 0
    for i in range(1, n+1):
        if i < 10:
            count += 1
        elif i < 100:
            if i % 11 == 0:
                count += 1
            else:
                count += 2
        elif i < 1000:
            if i % 11 == 0:
                count += 1
            else:
                count += 3
        elif i < 10000:
            if i % 11 == 0:
                count += 1
            else:
                count += 4
        elif i < 100000:
            if i % 11 == 0:
                count += 1
            else:
                count += 5
        elif i < 1000000:
            if i % 11 == 0:
                count += 1
            else:
                count += 6
        elif i < 10000000:
            if i % 11 == 0:
                count += 1
            else:
                count += 7
        elif i < 100000000:
            if i % 11 == 0:
                count += 1
            else:
                count += 8
        elif i < 1000000000:
            if i % 11 == 0:
                count += 1
            else:
                count += 9
        elif i < 10000000000:
            if i % 11 == 0:
                count += 1
            else:
                count += 10
        else:
            if i % 11 == 0:
                count += 1
            else:
                count += 11
    return count

=======
Suggestion 9

def solve(n):
    ans = 0
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if int(str(a)[-1]) == int(str(b)[0]) and int(str(a)[0]) == int(str(b)[-1]):
                ans += 1
    return ans
