Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    a, n = map(int, input().split())
    cnt = 0
    while n > 1:
        if n % a == 0:
            n //= a
            cnt += 1
        elif n % 10 == 0:
            n //= 10
            cnt += 1
        else:
            print(-1)
            return
    print(cnt)

=======
Suggestion 2

def main():
    a, n = map(int, input().split())
    ans = 0
    while n > 1:
        if n % a == 0:
            n //= a
        else:
            if n % 10 == 0:
                n //= 10
            else:
                print(-1)
                return
        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    a, N = map(int, input().split())
    count = 0
    while N > 1:
        if N % a == 0:
            N //= a
        elif N % 10 == 0:
            N //= 10
        else:
            break
        count += 1
    if N == 1:
        print(count)
    else:
        print(-1)

=======
Suggestion 4

def main():
    a, n = map(int, input().split())
    if n == 1:
        print(0)
        return
    if a == 2:
        print(len(bin(n)) - 3)
        return
    if a == 10:
        print(len(str(n)) - 1)
        return
    if n % a == 0:
        print(-1)
        return
    if n % a == 1:
        print(len(str(n)) - 1)
        return
    if n % a == 2:
        print(len(str(n)) - 1)
        return
    if n % a == 3:
        print(len(str(n)) - 1)
        return
    if n % a == 4:
        print(len(str(n)) - 1)
        return
    if n % a == 5:
        print(len(str(n)) - 1)
        return
    if n % a == 6:
        print(len(str(n)) - 1)
        return
    if n % a == 7:
        print(len(str(n)) - 1)
        return
    if n % a == 8:
        print(len(str(n)) - 1)
        return
    if n % a == 9:
        print(len(str(n)) - 1)
        return

=======
Suggestion 5

def main():
    a, n = map(int, input().split())
    ans = -1

    # 1 -> 2 -> 4 -> 8 -> 16 -> 32 -> 64 -> 46 -> 92 -> 29 -> 58 -> 116 -> 611
    # 1 -> 2 -> 4 -> 8 -> 16 -> 32 -> 64 -> 46 -> 92 -> 29 -> 58 -> 116 -> 611 -> 1222 -> 2444 -> 4888 -> 9776 -> 19552 -> 39104 -> 78208 -> 156416 -> 312832 -> 625664 -> 1251328 -> 2502656 -> 5005312 -> 10010624 -> 20021248 -> 40042496 -> 80084992 -> 160169984 -> 320339968 -> 640679936 -> 1281359872 -> 2562719744 -> 5125439488 -> 10250878976 -> 20501757952 -> 41003515904 -> 82007031808 -> 164014063616 -> 328028127232 -> 656056254464 -> 1312112508928 -> 2624225017856 -> 5248450035712 -> 10496900071424 -> 20993800142848 -> 41987600285696 -> 83975200571392 -> 167950401142784 -> 335900802285568 -> 671801604571136 -> 1343603209142272 -> 2687206418284544 -> 5374412836569088 -> 10748825673138176 -> 21497651346276352 -> 42995302692552704 -> 85990605385105408 -> 171981210770210816 -> 343962421540421632 -> 687924843080843264 -> 1375849686161686528 -> 2751699372323373056 -> 5503398744646746112 -> 11006797489293492224 -> 22013594978586984448 -> 44027189957173968896 -> 88054379914347937792 -> 176108759828695875584 -> 352217519657391751168 -> 704435039314783502336 -> 140887007862956700467

=======
Suggestion 6

def main():
    a, n = map(int, input().split())
    x = 1
    for i in range(1, 10**6):
        x = int(str(x)[-1] + str(x*a)[0])
        if x == n:
            print(i)
            return
    print(-1)
    return

=======
Suggestion 7

def count(a, n, count):
    if n == 1:
        return count
    elif n % a == 0:
        return count(a, n / a, count + 1)
    elif n % 10 != 0:
        return count(a, int(str(n % 10) + str(n // 10)), count + 1)
    else:
        return -1

a, n = map(int, input().split())
print(count(a, n, 0))

=======
Suggestion 8

def main():
    a, n = map(int, input().split())

    # 1
    if a == n:
        print(1)
        return

    # 2
    if a == 2:
        print(-1)
        return

    # 3
    if a == 3:
        if n % 3 == 0:
            print(n // 3)
        else:
            print(-1)
        return

    # 4
    if a == 4:
        if n % 4 == 0:
            print(n // 4)
        else:
            print(-1)
        return

    # 5
    if a == 5:
        if n % 5 == 0:
            print(n // 5)
        else:
            print(-1)
        return

    # 6
    if a == 6:
        if n % 6 == 0:
            print(n // 6)
        else:
            print(-1)
        return

    # 7
    if a == 7:
        if n % 7 == 0:
            print(n // 7)
        else:
            print(-1)
        return

    # 8
    if a == 8:
        if n % 8 == 0:
            print(n // 8)
        else:
            print(-1)
        return

    # 9
    if a == 9:
        if n % 9 == 0:
            print(n // 9)
        else:
            print(-1)
        return

    # 10
    if a == 10:
        if n % 10 == 0:
            print(n // 10)
        else:
            print(-1)
        return

    # 11
    if a == 11:
        if n % 11 == 0:
            print(n // 11)
        else:
            print(-1)
        return

    # 12
    if a == 12:
        if n % 12 == 0:
            print(n // 12)
        else:
            print(-1)
        return

    # 13
    if a == 13:
        if n % 13 == 0:
            print(n // 13)
        else:
            print(-1)
        return

    # 14
    if

=======
Suggestion 9

def main():
    a, N = map(int, input().split())
    if N == 1:
        print(0)
        return

    # 1回目の操作
    # 1 -> 3
    # 2 -> 4
    # 3 -> 6
    # 4 -> 8
    # 5 -> 10
    # 6 -> 12
    # 7 -> 14
    # 8 -> 16
    # 9 -> 18
    # 10 -> 20
    # 11 -> 22
    # 12 -> 24
    # 13 -> 26
    # 14 -> 28
    # 15 -> 30
    # 16 -> 32
    # 17 -> 34
    # 18 -> 36
    # 19 -> 38
    # 20 -> 40
    # 21 -> 42
    # 22 -> 44
    # 23 -> 46
    # 24 -> 48
    # 25 -> 50
    # 26 -> 52
    # 27 -> 54
    # 28 -> 56
    # 29 -> 58
    # 30 -> 60
    # 31 -> 62
    # 32 -> 64
    # 33 -> 66
    # 34 -> 68
    # 35 -> 70
    # 36 -> 72
    # 37 -> 74
    # 38 -> 76
    # 39 -> 78
    # 40 -> 80
    # 41 -> 82
    # 42 -> 84
    # 43 -> 86
    # 44 -> 88
    # 45 -> 90
    # 46 -> 92
    # 47 -> 94
    # 48 -> 96
    # 49 -> 98
    # 50 -> 100
    # 51 -> 102
    # 52 -> 104
    # 53 -> 106
    # 54 -> 108
    # 55 -> 110
    # 56 -> 112
    # 57 -> 114
    # 58 ->
