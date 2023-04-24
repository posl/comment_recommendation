Synthesizing 9/10 solutions

=======
Suggestion 1

def dfs(s):
    if int(s) > N:
        return 0
    ret = 1 if all(s.count(c) > 0 for c in '753') else 0
    for c in '753':
        ret += dfs(s + c)
    return ret

N = int(input())
print(dfs('0'))

=======
Suggestion 2

def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        if "7" in str(i) or "5" in str(i) or "3" in str(i):
            count += 1
    print(count)

main()

=======
Suggestion 3

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        if "7" in str(i) or "5" in str(i) or "3" in str(i):
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    count = 0
    for i in range(1, N + 1):
        if '7' in str(i) or '5' in str(i) or '3' in str(i):
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    if N < 357:
        print(0)
    elif N < 537:
        print(1)
    elif N < 573:
        print(2)
    elif N < 735:
        print(3)
    elif N < 753:
        print(4)
    elif N < 3357:
        print(5)
    elif N < 3375:
        print(6)
    elif N < 3537:
        print(7)
    elif N < 3557:
        print(8)
    elif N < 3573:
        print(9)
    elif N < 3575:
        print(10)
    elif N < 3577:
        print(11)
    elif N < 3735:
        print(12)
    elif N < 3753:
        print(13)
    elif N < 5337:
        print(14)
    elif N < 5357:
        print(15)
    elif N < 5373:
        print(16)
    elif N < 5375:
        print(17)
    elif N < 5377:
        print(18)
    elif N < 5733:
        print(19)
    elif N < 5735:
        print(20)
    elif N < 7335:
        print(21)
    elif N < 7353:
        print(22)
    elif N < 7533:
        print(23)
    elif N < 33557:
        print(24)
    elif N < 33575:
        print(25)
    elif N < 33753:
        print(26)
    elif N < 33775:
        print(27)
    elif N < 35357:
        print(28)
    elif N < 35375:
        print(29)
    elif N < 35573:
        print(30)
    elif N < 35575:
        print(31)
    elif N < 35733:
        print(32)
    elif N < 35735:
        print(33)
    elif N < 35737:
        print(34)
    elif N < 35753:
        print(35)
    elif N < 35755:
        print(36)
    elif N < 35757:
        print(37)
    elif N

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if '7' in str(i) or '5' in str(i) or '3' in str(i):
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        if "3" in str(i) and "5" in str(i) and "7" in str(i):
            cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    N = int(input())
    N = N + 1
    n = 0
    for i in range(1, N):
        if '7' in str(i) and '5' in str(i) and '3' in str(i):
            n = n + 1
    print(n)

=======
Suggestion 9

def main():
    N = int(input())
    print(calc(N))
