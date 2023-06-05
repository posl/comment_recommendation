Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    time = [a,b,c,d,e]
    time.sort()
    for i in range(5):
        if time[i] % 10 != 0:
            time[i] = time[i] + 10 - time[i] % 10
    print(time[4])

=======
Suggestion 2

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print(10 * ((A + 9) // 10) + 10 * ((B + 9) // 10) + 10 * ((C + 9) // 10) + 10 * ((D + 9) // 10) + 10 * ((E + 9) // 10) - 50)

=======
Suggestion 3

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print(min([A,B,C,D,E], key=lambda x: x % 10) + sum([10 * ((x - 1) // 10 + 1) for x in [A,B,C,D,E]]))

=======
Suggestion 4

def problems123_b():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    min_time = min(A, B, C, D, E)
    if min_time == A:
        min_time = 0
    elif min_time == B:
        min_time = 10
    elif min_time == C:
        min_time = 20
    elif min_time == D:
        min_time = 30
    else:
        min_time = 40

    if A % 10 == 0:
        A = A
    else:
        A = A + (10 - A % 10)

    if B % 10 == 0:
        B = B
    else:
        B = B + (10 - B % 10)

    if C % 10 == 0:
        C = C
    else:
        C = C + (10 - C % 10)

    if D % 10 == 0:
        D = D
    else:
        D = D + (10 - D % 10)

    if E % 10 == 0:
        E = E
    else:
        E = E + (10 - E % 10)

    print(A + B + C + D + E - 50 + min_time)

=======
Suggestion 5

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    a = A % 10
    b = B % 10
    c = C % 10
    d = D % 10
    e = E % 10

    if a == 0:
        pass
    else:
        A = A + (10 - a)
    if b == 0:
        pass
    else:
        B = B + (10 - b)
    if c == 0:
        pass
    else:
        C = C + (10 - c)
    if d == 0:
        pass
    else:
        D = D + (10 - d)
    if e == 0:
        pass
    else:
        E = E + (10 - e)

    if A == B == C == D == E:
        print(A)
    elif A > B and A > C and A > D and A > E:
        print(A)
    elif B > A and B > C and B > D and B > E:
        print(B)
    elif C > A and C > B and C > D and C > E:
        print(C)
    elif D > A and D > B and D > C and D > E:
        print(D)
    elif E > A and E > B and E > C and E > D:
        print(E)

=======
Suggestion 6

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    t = [a,b,c,d,e]
    m = 0
    for i in range(5):
        if m < t[i]%10:
            m = t[i]%10
            n = i
    for i in range(5):
        if i != n:
            t[i] = t[i] + 10 - t[i]%10
    print(sum(t))

=======
Suggestion 7

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print((a + 9) // 10 * 10 + (b + 9) // 10 * 10 + (c + 9) // 10 * 10 + (d + 9) // 10 * 10 + (e + 9) // 10 * 10)

=======
Suggestion 8

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    if a%10 == 0:
        a = a
    else:
        a = (a//10 + 1)*10
    if b%10 == 0:
        b = b
    else:
        b = (b//10 + 1)*10
    if c%10 == 0:
        c = c
    else:
        c = (c//10 + 1)*10
    if d%10 == 0:
        d = d
    else:
        d = (d//10 + 1)*10
    if e%10 == 0:
        e = e
    else:
        e = (e//10 + 1)*10
    print(a+b+c+d+e)

=======
Suggestion 9

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(10*((a-1)//10+(b-1)//10+(c-1)//10+(d-1)//10+(e-1)//10)+max(a%10,b%10,c%10,d%10,e%10))

=======
Suggestion 10

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    # 1. 一开始就点饭碗
    # 2. 一开始就点咖喱
    # 3. 一开始就点意大利面
    # 4. 一开始就点拉面
    # 5. 一开始就点汉堡饼
    # 6. 一开始就点饭碗，第二个点咖喱
    # 7. 一开始就点饭碗，第二个点意大利面
    # 8. 一开始就点饭碗，第二个点拉面
    # 9. 一开始就点饭碗，第二个点汉堡饼
    # 10. 一开始就点咖喱，第二个点意大利面
    # 11. 一开始就点咖喱，第二个点拉面
    # 12. 一开始就点咖喱，第二个点汉堡饼
    # 13. 一开始就点意大利面，第二个点拉面
    # 14. 一开始就点意大利面，第二个点汉堡饼
    # 15. 一开始就点拉面，第二个点汉堡饼
    # 16. 一开始就点饭碗，第二个点咖喱，第三个点意大利面
    # 17. 一开始就点饭碗，第二个点咖喱，第三个点拉面
    # 18. 一开始就点饭碗，第二个点咖喱，第三个点汉堡饼
    # 19. 一开始就点饭碗，第二个点意大利面，第三个点拉面
