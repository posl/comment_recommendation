def main():
    A,B = [int(x) for x in input().split()]
    if A < 6:
        print(0)
    elif 6 <= A <= 12:
        print(B//2)
    else:
        print(B)
