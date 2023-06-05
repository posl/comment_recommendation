def problem212_a():
    A,B = map(int,input().split())
    if A > 0 and B == 0:
        print("黄金")
    elif A == 0 and B > 0:
        print("银")
    else:
        print("合金")

if __name__ == '__main__':
    problem212_a()