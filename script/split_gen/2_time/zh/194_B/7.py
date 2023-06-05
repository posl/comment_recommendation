def main():
    A, B = map(int, input().split())
    if A == 0:
        print(4)
    elif B == 0:
        print(3)
    elif A + B < 15:
        print(4)
    elif A + B >= 15 and B >= 8:
        print(1)
    elif A + B >= 10 and B >= 3:
        print(2)
    else:
        print(4)
