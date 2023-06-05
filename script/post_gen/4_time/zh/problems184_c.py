Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    r1,c1 = map(int,input().split())
    r2,c2 = map(int,input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        exit()
    if r1+c1 == r2+c2 or r1-c1 == r2-c2 or abs(r1-r2)+abs(c1-c2) <= 3:
        print(1)
        exit()
    if (r1+c1)%2 == (r2+c2)%2:
        print(2)
        exit()
    for i in range(-3,4):
        for j in range(-3,4):
            if abs(i)+abs(j) <= 3:
                if (r1+i+c1+j)%2 == (r2+c2)%2:
                    print(2)
                    exit()
    print(3)

=======
Suggestion 3

def main():
    # 读入数据
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    # 处理
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return
    for i in range(-3, 4):
        for j in range(-3, 4):
            if abs(i) + abs(j) <= 3:
                if r1 + i + c1 + j == r2 + c2:
                    print(2)
                    return
    print(3)
    return

=======
Suggestion 4

def main():
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    if (x1+y1) == (x2+y2) or (x1-y1) == (x2-y2):
        print(1)
    elif abs(x1-x2)+abs(y1-y2) <= 3:
        print(1)
    elif (x1+y1)%2 == (x2+y2)%2:
        print(2)
    elif abs((x1+y1)-(x2+y2)) <= 3:
        print(2)
    elif abs((x1-y1)-(x2-y2)) <= 3:
        print(2)
    else:
        print(3)

=======
Suggestion 5

def main():
    r_1, c_1 = map(int, input().split())
    r_2, c_2 = map(int, input().split())
    if r_1 == r_2 and c_1 == c_2:
        print(0)
        return
    if r_1 + c_1 == r_2 + c_2 or r_1 - c_1 == r_2 - c_2 or abs(r_1 - r_2) + abs(c_1 - c_2) <= 3:
        print(1)
        return
    if (r_1 + c_1) % 2 == (r_2 + c_2) % 2:
        print(2)
        return
    for i in range(-3, 4):
        for j in range(-3, 4):
            if abs(i - j) % 2 == 0:
                continue
            if abs(i) + abs(j) <= 3:
                continue
            if r_1 + i + c_1 + j == r_2 + c_2 or r_1 + i - c_1 - j == r_2 - c_2 or abs(r_1 + i - r_2) + abs(c_1 + j - c_2) <= 3:
                print(2)
                return
    print(3)
    return

=======
Suggestion 6

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    if r1 == r2 and c1 == c2:
        print(0)
        return

    if (r1 + c1 == r2 + c2) or (r1 - c1 == r2 - c2) or (abs(r1 - r2) + abs(c1 - c2) <= 3):
        print(1)
        return

    if (r1 + c1 + r2 + c2) % 2 == 0:
        print(2)
        return

    for i in range(-3, 4):
        for j in range(-3, 4):
            r3 = r1 + i
            c3 = c1 + j
            if (r3 + c3 == r2 + c2) or (r3 - c3 == r2 - c2) or (abs(r3 - r2) + abs(c3 - c2) <= 3):
                print(2)
                return

    print(3)

=======
Suggestion 7

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if (r1 == r2 and c1 == c2):
        print(0)
        return
    if (r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3):
        print(1)
        return
    if ((r1 + c1) % 2 == (r2 + c2) % 2):
        print(2)
        return
    for i in range(-3, 4):
        for j in range(-3, 4):
            if (abs(i) + abs(j) == 3):
                if (r1 + i + c1 + j == r2 + c2 or r1 + i - c1 - j == r2 - c2 or abs(r1 + i - r2) + abs(c1 + j - c2) <= 3):
                    print(2)
                    return
    print(3)

=======
Suggestion 8

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if r1 + c1 == r2 + c2:
        print(1)
        return
    if r1 - c1 == r2 - c2:
        print(1)
        return
    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        return
    for i in range(-3, 4):
        for j in range(-3, 4):
            if (r1 + i + c1 + j) % 2 == (r2 + c2) % 2:
                if abs(i) + abs(j) <= 3:
                    print(2)
                    return
    print(3)
    return
