Synthesizing 10/10 solutions

=======
Suggestion 1

def judge7(n):
    if n%7==0:
        return True
    while n>0:
        if n%10==7:
            return True
        n=n//10
    return False

=======
Suggestion 2

def main():
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        if "7" in str(i) or "7" in oct(i):
            continue
        else:
            count += 1
    print(count)

=======
Suggestion 3

def check7(n):
    if n.find('7') == -1:
        return True
    else:
        return False

=======
Suggestion 4

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        if "7" in str(i):
            continue
        if "7" in str(oct(i)):
            continue
        count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        if '7' in str(i) or '7' in oct(i):
            continue
        count+=1
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if '7' in str(i) or '7' in oct(i):
            count += 1
    print(n - count)

=======
Suggestion 7

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if '7' in str(i) or '7' in oct(i):
            pass
        else:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        if '7' in str(i):
            continue
        if '7' in oct(i):
            continue
        cnt += 1
    print(cnt)

=======
Suggestion 9

def main():
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        if '7' not in str(i) and '7' not in oct(i):
            count += 1
    print(count)

=======
Suggestion 10

def count7(n):
    count = 0
    for i in range(n+1):
        if '7' in str(i) or '7' in oct(i):
            count += 1
    return count
