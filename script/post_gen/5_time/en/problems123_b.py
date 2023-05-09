Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    a = (a+9)//10*10
    b = (b+9)//10*10
    c = (c+9)//10*10
    d = (d+9)//10*10
    e = (e+9)//10*10
    print(a+b+c+d+e)

=======
Suggestion 2

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print((A-1)//10*10 + A + (B-1)//10*10 + B + (C-1)//10*10 + C + (D-1)//10*10 + D + (E-1)//10*10 + E)

=======
Suggestion 3

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    min_time = min(A, B, C, D, E)
    if min_time == A or min_time == B or min_time == C or min_time == D:
        min_time = min_time + 10
    else:
        pass

    if min_time == A or min_time == B or min_time == C or min_time == D:
        min_time = min_time + 10
    else:
        pass

    if min_time == A or min_time == B or min_time == C or min_time == D:
        min_time = min_time + 10
    else:
        pass

    if min_time == A or min_time == B or min_time == C or min_time == D:
        min_time = min_time + 10
    else:
        pass

    if min_time == A or min_time == B or min_time == C or min_time == D:
        min_time = min_time + 10
    else:
        pass

    print(min_time)

=======
Suggestion 4

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    min_time = min(a, b, c, d, e)

    if a % 10 == 0:
        a_time = a
    else:
        a_time = (a // 10 + 1) * 10

    if b % 10 == 0:
        b_time = b
    else:
        b_time = (b // 10 + 1) * 10

    if c % 10 == 0:
        c_time = c
    else:
        c_time = (c // 10 + 1) * 10

    if d % 10 == 0:
        d_time = d
    else:
        d_time = (d // 10 + 1) * 10

    if e % 10 == 0:
        e_time = e
    else:
        e_time = (e // 10 + 1) * 10

    time = a_time + b_time + c_time + d_time + e_time - min_time

    print(time)

=======
Suggestion 5

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    print(min([((A+9)//10)*10,((B+9)//10)*10,((C+9)//10)*10,((D+9)//10)*10,((E+9)//10)*10])+E)

=======
Suggestion 6

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    l = [a,b,c,d,e]
    l.sort()
    for i in range(len(l)):
        if l[i]%10 == 0:
            continue
        else:
            l[i] = l[i] + (10 - (l[i]%10))
    print(sum(l)-10)
    return 0

=======
Suggestion 7

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    time = 0
    time += a
    if time % 10 != 0:
        time += 10 - time % 10
    time += b
    if time % 10 != 0:
        time += 10 - time % 10
    time += c
    if time % 10 != 0:
        time += 10 - time % 10
    time += d
    if time % 10 != 0:
        time += 10 - time % 10
    time += e
    print(time)

=======
Suggestion 8

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    timeList = [A,B,C,D,E]
    timeList.sort()
    timeList = timeList[1:]
    time = 0
    for t in timeList:
        if t % 10 != 0:
            time += t + 10 - (t % 10)
        else:
            time += t
    print(time)

=======
Suggestion 9

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    #print(a,b,c,d,e)
    a = a % 10
    b = b % 10
    c = c % 10
    d = d % 10
    e = e % 10
    #print(a,b,c,d,e)
    if a == 0:
        a = 10
    if b == 0:
        b = 10
    if c == 0:
        c = 10
    if d == 0:
        d = 10
    if e == 0:
        e = 10
    #print(a,b,c,d,e)
    if a == 10:
        a = 0
    if b == 10:
        b = 0
    if c == 10:
        c = 0
    if d == 10:
        d = 0
    if e == 10:
        e = 0
    #print(a,b,c,d,e)
    a = a + b + c + d + e
    print(a)
    return 0

=======
Suggestion 10

def main():
    # Get the input
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    # Calculate the time
    if a % 10 != 0:
        a += 10 - (a % 10)
    if b % 10 != 0:
        b += 10 - (b % 10)
    if c % 10 != 0:
        c += 10 - (c % 10)
    if d % 10 != 0:
        d += 10 - (d % 10)
    if e % 10 != 0:
        e += 10 - (e % 10)
    # Calculate the time
    time = a + b + c + d + e
    # Print the time
    print(time)

main()
