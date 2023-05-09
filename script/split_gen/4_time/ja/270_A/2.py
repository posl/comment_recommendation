def main():
    a = input()
    a = a.split()
    A = int(a[0])
    B = int(a[1])
    if A == 0 and B == 0:
        print(0)
    elif A == 1 and B == 0:
        print(1)
    elif A == 0 and B == 1:
        print(1)
    elif A == 2 and B == 0:
        print(2)
    elif A == 0 and B == 2:
        print(2)
    elif A == 1 and B == 1:
        print(2)
    elif A == 4 and B == 0:
        print(4)
    elif A == 0 and B == 4:
        print(4)
    elif A == 3 and B == 0:
        print(3)
    elif A == 0 and B == 3:
        print(3)
    elif A == 2 and B == 1:
        print(3)
    elif A == 1 and B == 2:
        print(3)
    elif A == 2 and B == 2:
        print(4)
    elif A == 4 and B == 1:
        print(5)
    elif A == 1 and B == 4:
        print(5)
    elif A == 3 and B == 1:
        print(4)
    elif A == 1 and B == 3:
        print(4)
    elif A == 2 and B == 3:
        print(5)
    elif A == 3 and B == 2:
        print(5)
    elif A == 4 and B == 2:
        print(6)
    elif A == 2 and B == 4:
        print(6)
    elif A == 3 and B == 3:
        print(6)
    elif A == 4 and B == 3:
        print(7)
    elif A == 3 and B == 4:
        print(7)
    elif A == 4 and B == 4:
        print(8)
