def main():
    N, A, B = map(int, input().split())
    if N == 1:
        if A > 0:
            print(1)
        else:
            print(0)
        return
    if A > B:
        print(0)
        return
    if A == 0 and B > 0:
        print(0)
        return
    if A == 0 and B == 0:
        print(0)
        return
    if A == B:
        print(1)
        return
    if A < B:
        if N == 2:
            print(1)
            return
        if N == 3:
            print(2)
            return
        if N == 4:
            print(2)
            return
        if N == 5:
            print(3)
            return
        if N == 6:
            print(3)
            return
        if N == 7:
            print(4)
            return
        if N == 8:
            print(4)
            return
        if N == 9:
            print(5)
            return
        if N == 10:
            print(5)
            return
        if N == 11:
            print(6)
            return
        if N == 12:
            print(6)
            return
        if N == 13:
            print(7)
            return
        if N == 14:
            print(7)
            return
        if N == 15:
            print(8)
            return
        if N == 16:
            print(8)
            return
        if N == 17:
            print(9)
            return
        if N == 18:
            print(9)
            return
        if N == 19:
            print(10)
            return
        if N == 20:
            print(10)
            return
        if N == 21:
            print(11)
            return
        if N == 22:
            print(11)
            return
        if N == 23:
            print(12)
            return
        if N == 24:
            print(12)
            return
        if N == 25:
            print(13)
            return
        if N == 26:
            print(13)
            return
        if N ==
