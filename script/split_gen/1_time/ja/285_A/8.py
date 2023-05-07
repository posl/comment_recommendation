def main():
    a, b = map(int, input().split())
    if a < b:
        if a == 1 and b == 2 or a == 2 and b == 1:
            print("Yes")
        elif a == 3 and b == 4 or a == 4 and b == 3:
            print("Yes")
        elif a == 5 and b == 6 or a == 6 and b == 5:
            print("Yes")
        elif a == 7 and b == 8 or a == 8 and b == 7:
            print("Yes")
        elif a == 9 and b == 10 or a == 10 and b == 9:
            print("Yes")
        elif a == 11 and b == 12 or a == 12 and b == 11:
            print("Yes")
        elif a == 13 and b == 14 or a == 14 and b == 13:
            print("Yes")
        elif a == 15 and b == 16 or a == 16 and b == 15:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
