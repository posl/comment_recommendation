def main():
    S = input()
    l = len(S)
    if l == 1:
        print(0)
        return
    if l == 2:
        if int(S) < 10:
            print(1)
            return
        else:
            print(2)
            return
    if l == 3:
        if int(S) < 100:
            print(2)
            return
        else:
            print(3)
            return
    if l == 4:
        if int(S) < 1000:
            print(3)
            return
        else:
            print(4)
            return
    if l == 5:
        if int(S) < 10000:
            print(4)
            return
        else:
            print(5)
            return
    if l == 6:
        if int(S) < 100000:
            print(5)
            return
        else:
            print(6)
            return
    if l == 7:
        if int(S) < 1000000:
            print(6)
            return
        else:
            print(7)
            return
    if l == 8:
        if int(S) < 10000000:
            print(7)
            return
        else:
            print(8)
            return
    if l == 9:
        if int(S) < 100000000:
            print(8)
            return
        else:
            print(9)
            return
    if l == 10:
        if int(S) < 1000000000:
            print(9)
            return
        else:
            print(10)
            return
    if l == 11:
        if int(S) < 10000000000:
            print(10)
            return
        else:
            print(11)
            return
    if l == 12:
        if int(S) < 100000000000:
            print(11)
            return
        else:
            print(12)
            return
    if l == 13:
        if int(S) < 1000000000000:
            print(12)
            return
        else:
            print(13)
            return
    if l == 14:
        if int(S) < 10000000000000:
            print(13)
            return
        else
