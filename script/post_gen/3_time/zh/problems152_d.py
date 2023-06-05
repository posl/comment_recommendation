Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    cnt = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i > N or j > N:
                continue
            if str(i) == str(j):
                cnt += 1
    for i in range(1, 10):
        for j in range(1, 10):
            if i > N or j > N:
                continue
            if str(i) == str(j):
                cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if i < 10:
            count += 1
        else:
            num = str(i)
            if num[0] == num[-1]:
                count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    a = 0
    for i in range(1,n+1):
        if i < 10:
            a += 1
        elif i < 100:
            if i % 11 == 0:
                a += 1
        elif i < 1000:
            if i % 11 == 0:
                a += 2
        elif i < 10000:
            if i % 11 == 0:
                a += 3
        elif i < 100000:
            if i % 11 == 0:
                a += 4
        else:
            if i % 11 == 0:
                a += 5
    print(a)

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i % 10 == 0:
            continue
        s = str(i)
        a = int(s[0])
        b = int(s[len(s)-1])
        if a > b:
            continue
        for j in range(1, N+1):
            if j % 10 == 0:
                continue
            if a == j % 10 and b == int(str(j)[0]):
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    num = int(input())
    count = 0
    for i in range(1,num+1):
        for j in range(1,num+1):
            if i%10 == j//10 and j%10 == i//10:
                count += 1
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    if n < 10:
        print(n)
        return
    if n < 100:
        print(9)
        return
    if n < 1000:
        print(9 + n - 99)
        return
    if n < 10000:
        print(9 + 900)
        return
    if n < 100000:
        print(9 + 900 + n - 9999)
        return
    print(9 + 900 + 90000)

main()

=======
Suggestion 7

def count_pair(n):
    count = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if str(i)[0] == str(j)[-1] and str(i)[-1] == str(j)[0]:
                count += 1
    return count

=======
Suggestion 8

def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        s = str(i)
        ans += len(s) % 2
        if s[0: len(s) // 2] == s[len(s) // 2: len(s)][::-1]:
            ans += 1
    print(ans)

=======
Suggestion 9

def count(N):
    count = 0
    for i in range(1, N+1):
        if i < 10:
            count += 1
        else:
            if i % 10 == int(str(i)[0]):
                count += 1
    return count

=======
Suggestion 10

def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if i % 10 == 0:
            continue
        for j in range(1, n + 1):
            if j % 10 == 0:
                continue
            if str(i)[0] == str(j)[-1] and str(i)[-1] == str(j)[0]:
                ans += 1
    print(ans)
