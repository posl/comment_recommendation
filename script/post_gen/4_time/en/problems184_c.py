Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1) % 2 == (r2 + c2) % 2 or abs(r1 + c1 - r2 - c2) <= 3 or abs(r1 - c1 - r2 + c2) <= 3:
        print(2)
        return
    print(3)
    return

=======
Suggestion 2

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1) % 2 == (r2 + c2) % 2 or abs(r1 + c1 - r2 - c2) <= 3 or abs(r1 - c1 - r2 + c2) <= 3:
        print(2)
        return
    print(3)

=======
Suggestion 3

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
    elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
    elif (r1 + c1) % 2 == (r2 + c2) % 2 or abs(r1 - r2) + abs(c1 - c2) <= 6 or abs((r1 + c1) - (r2 + c2)) <= 3 or abs((r1 - c1) - (r2 - c2)) <= 3:
        print(2)
    else:
        print(3)

=======
Suggestion 4

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    if r1 == r2 and c1 == c2:
        print(0)
        exit()
    if r1 + c1 == r2 + c2:
        print(1)
        exit()
    if r1 - c1 == r2 - c2:
        print(1)
        exit()
    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        exit()
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        exit()
    if abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
        exit()
    if abs((r1 + c1) - (r2 + c2)) <= 3:
        print(2)
        exit()
    if abs((r1 - c1) - (r2 - c2)) <= 3:
        print(2)
        exit()
    print(3)

=======
Suggestion 5

def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    if r1 == r2 and c1 == c2:
        print(0)
        return

    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return

    if (r1 + c1) % 2 == (r2 + c2) % 2 or abs(r1 - r2) + abs(c1 - c2) <= 6 or abs(r1 + c1 - r2 - c2) <= 3 or abs(r1 - c1 - r2 + c2) <= 3:
        print(2)
        return

    print(3)

=======
Suggestion 6

def main():
    r_1, c_1 = map(int, input().split())
    r_2, c_2 = map(int, input().split())

    if(r_1 == r_2 and c_1 == c_2):
        print(0)
    elif(r_1 + c_1 == r_2 + c_2 or r_1 - c_1 == r_2 - c_2 or abs(r_1 - r_2) + abs(c_1 - c_2) <= 3):
        print(1)
    elif((r_1 + c_1 + r_2 + c_2) % 2 == 0 or abs((r_1 + c_1) - (r_2 + c_2)) <= 3 or abs((r_1 - c_1) - (r_2 - c_2)) <= 3 or abs(r_1 - r_2) + abs(c_1 - c_2) <= 6):
        print(2)
    else:
        print(3)

=======
Suggestion 7

def main():
    r1,c1 = map(int,input().split())
    r2,c2 = map(int,input().split())
    if r1==r2 and c1==c2:
        print(0)
    elif (r1+c1==r2+c2) or (r1-c1==r2-c2) or (abs(r1-r2)+abs(c1-c2)<=3):
        print(1)
    elif (r1+c1)%2==(r2+c2)%2:
        print(2)
    else:
        for i in range(-3,4):
            for j in range(-3,4):
                if (r1+i+c1+j==r2+c2) or (r1+i-c1-j==r2-c2) or (abs(r1+i-r2)+abs(c1+j-c2)<=3):
                    print(2)
                    exit()
        print(3)

=======
Suggestion 8

def main():
    r1,c1 = map(int,input().split())
    r2,c2 = map(int,input().split())
    if r1==r2 and c1==c2:
        print(0)
        return
    elif abs(r1-r2)+abs(c1-c2) <= 3:
        print(1)
        return
    elif (r1+c1)%2 == (r2+c2)%2:
        print(2)
        return
    else:
        for i in range(-3,4):
            for j in range(-3,4):
                if abs(i)+abs(j) <= 3:
                    if (r1+i+c1+j)%2 == (r2+c2)%2:
                        print(2)
                        return
        print(3)
        return

=======
Suggestion 9

def main():
    # Take input Here and Call solution function
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        return
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        return
    if (r1 + c1 + r2 + c2) % 2 == 0:
        print(2)
        return
    for i in range(-3, 4):
        for j in range(-3, 4):
            if abs(i) + abs(j) <= 3:
                x = r1 + i
                y = c1 + j
                if abs(r2 - x) + abs(c2 - y) <= 6:
                    print(2)
                    return
    print(3)
    return
