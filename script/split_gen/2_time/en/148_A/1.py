def main():
    A = int(input())
    B = int(input())
    C = 0
    if A == 1:
        if B == 2:
            C = 3
        else:
            C = 2
    elif A == 2:
        if B == 1:
            C = 3
        else:
            C = 1
    else:
        if B == 1:
            C = 2
        else:
            C = 1
    print(C)
