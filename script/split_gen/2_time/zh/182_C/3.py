def main():
    n = input()
    k = len(n)
    s = 0
    for i in range(k):
        s += int(n[i])
    if s%3 == 0:
        print(0)
    elif k == 1:
        print(-1)
    elif k == 2:
        print(-1)
    elif k == 3:
        print(-1)
    else:
        if s%3 == 1:
            if n.count('1') > 0:
                print(1)
            elif n.count('4') > 0:
                print(1)
            elif n.count('7') > 0:
                print(1)
            elif n.count('2') > 1:
                print(2)
            elif n.count('5') > 1:
                print(2)
            elif n.count('8') > 1:
                print(2)
            else:
                print(-1)
        else:
            if n.count('2') > 0:
                print(1)
            elif n.count('5') > 0:
                print(1)
            elif n.count('8') > 0:
                print(1)
            elif n.count('1') > 1:
                print(2)
            elif n.count('4') > 1:
                print(2)
            elif n.count('7') > 1:
                print(2)
            else:
                print(-1)
