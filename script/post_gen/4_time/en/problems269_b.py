Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = []
    for i in range(10):
        s.append(input())
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        if s[i].count('#') == 0:
            continue
        if a == 0:
            a = i+1
            b = i+1
            c = s[i].index('#')+1
            d = s[i].rindex('#')+1
        else:
            b = i+1
            c = min(c, s[i].index('#')+1)
            d = max(d, s[i].rindex('#')+1)
    print(a, b)
    print(c, d)

=======
Suggestion 2

def main():
    s = [input() for _ in range(10)]
    a, b, c, d = -1, -1, -1, -1
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                if a < 0:
                    a = i
                b = i
                if c < 0:
                    c = j
                d = j
    print(a + 1, b + 1)
    print(c + 1, d + 1)

=======
Suggestion 3

def main():
    S = [input() for _ in range(10)]
    A = B = C = D = 0
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                if A == 0:
                    A = i+1
                if B < i+1:
                    B = i+1
                if C == 0:
                    C = j+1
                if D < j+1:
                    D = j+1
    print(A,B)
    print(C,D)

=======
Suggestion 4

def readinput():
    s=[]
    for i in range(10):
        s.append(input())
    return s

=======
Suggestion 5

def main():
    S = []
    for i in range(10):
        S.append(input())

    for i in range(10):
        if '#' in S[i]:
            a = i
            break

    for i in range(9, -1, -1):
        if '#' in S[i]:
            b = i
            break

    for i in range(10):
        if '#' in S[i]:
            c = S[i].index('#')
            break

    for i in range(9, -1, -1):
        if '#' in S[i]:
            d = S[i].rindex('#')
            break

    print(a + 1, b + 1)
    print(c + 1, d + 1)

=======
Suggestion 6

def main():
    dots = []
    for i in range(10):
        dots.append(input())
    for i in range(10):
        dots[i] = dots[i].replace('.', '0')
        dots[i] = dots[i].replace('#', '1')
        dots[i] = list(map(int, dots[i]))
    dots = list(map(list, zip(*dots)))
    for i in range(10):
        dots[i] = list(map(str, dots[i]))
        dots[i] = ''.join(dots[i])
        dots[i] = dots[i].replace('0', '.')
        dots[i] = dots[i].replace('1', '#')
    for i in range(10):
        print(dots[i])

=======
Suggestion 7

def main():
    #print("Hello World!")
    s = []
    for i in range(10):
        s.append(input())
    #print(s)
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        if "#" in s[i]:
            a = i+1
            break
    for i in range(9, -1, -1):
        if "#" in s[i]:
            b = i+1
            break
    #print(a)
    #print(b)
    for i in range(10):
        if "#" in s[i]:
            c = s[i].index("#")+1
            break
    for i in range(9, -1, -1):
        if "#" in s[i]:
            d = s[i].index("#")+1
            break
    #print(c)
    #print(d)
    print(str(a)+" "+str(b))
    print(str(c)+" "+str(d))
    return 0

=======
Suggestion 8

def main():
    #s = [input() for _ in range(10)]
    #s = [input() for _ in range(10)]
    s = []
    for _ in range(10):
        s.append(input())

    #print(s)

    for i in range(10):
        s[i] = s[i].replace(".", "0")
        s[i] = s[i].replace("#", "1")

    #print(s)

    s = [int(i) for i in s]

    #print(s)

    for i in range(10):
        if s[i] == 1:
            s[i] = 0
        else:
            s[i] = 1

    #print(s)

    for i in range(10):
        s[i] = str(s[i])

    #print(s)

    for i in range(10):
        s[i] = s[i].replace("0", ".")
        s[i] = s[i].replace("1", "#")

    #print(s)

    for i in range(10):
        print(s[i])

=======
Suggestion 9

def main():
    # Read from Standard Input
    s = [input() for i in range(10)]

    # Process
    for i in range(10):
        s[i] = s[i].replace(".", "0")
        s[i] = s[i].replace("#", "1")
        s[i] = int(s[i], 2)

    for a in range(10):
        for b in range(a, 10):
            for c in range(10):
                for d in range(c, 10):
                    if all(((s[i] >> d) & 1) == 0 for i in range(a, b+1)) and all(((s[i] >> j) & 1) == 1 for i in range(a, b+1) for j in range(c, d+1)):
                        print(a+1, b+1)
                        print(c+1, d+1)
                        exit()

=======
Suggestion 10

def main():
    s = []
    for i in range(10):
        s.append(input())

    # print(s)

    for i in range(10):
        if s[i].count('.') == 10:
            row = i
            break

    # print(row)

    for i in range(10):
        if s[i][row] == '#':
            col = i
            break

    # print(col)

    for i in range(row):
        if s[col][i] == '#':
            row -= 1
        else:
            break

    # print(row)

    for i in range(col):
        if s[i][row] == '#':
            col -= 1
        else:
            break

    # print(col)

    print(col + 1, row + 1)
