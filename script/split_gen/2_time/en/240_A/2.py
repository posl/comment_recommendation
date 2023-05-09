def main():
    a, b = map(int, input().split())
    if (a == 1 or a == 9 or a == 7 or a == 4) and (b == 1 or b == 9 or b == 7 or b == 4):
        print("Yes")
    elif (a == 2 or a == 5 or a == 8 or a == 0) and (b == 2 or b == 5 or b == 8 or b == 0):
        print("Yes")
    elif (a == 3 or a == 6) and (b == 3 or b == 6):
        print("Yes")
    else:
        print("No")
