def solve():
    A,B = map(int,input().split())
    C = 0
    if A == 0 and B == 0:
        C = 0
    elif A == 0 and B == 1:
        C = 2
    elif A == 0 and B == 2:
        C = 4
    elif A == 0 and B == 3:
        C = 6
    elif A == 0 and B == 4:
        C = 8
    elif A == 0 and B == 5:
        C = 10
    elif A == 0 and B == 6:
        C = 12
    elif A == 0 and B == 7:
        C = 14
    elif A == 1 and B == 0:
        C = 1
    elif A == 1 and B == 1:
        C = 3
    elif A == 1 and B == 2:
        C = 5
    elif A == 1 and B == 3:
        C = 7
    elif A == 1 and B == 4:
        C = 9
    elif A == 1 and B == 5:
        C = 11
    elif A == 1 and B == 6:
        C = 13
    elif A == 1 and B == 7:
        C = 15
    elif A == 2 and B == 0:
        C = 2
    elif A == 2 and B == 1:
        C = 3
    elif A == 2 and B == 2:
        C = 6
    elif A == 2 and B == 3:
        C = 7
    elif A == 2 and B == 4:
        C = 10
    elif A == 2 and B == 5:
        C = 11
    elif A == 2 and B == 6:
        C = 14
    elif A == 2 and B == 7:
        C = 15
    elif A == 3 and B == 0:
        C = 4
    elif A == 3 and B == 1:
        C = 5
    elif A == 3 and B == 2:
        C

if __name__ == '__main__':
    solve()