def main():
    a,b = map(int, input().split())
    if a == 8 or a == 9:
        if b == 8 or b == 9:
            print("Yes")
            return
    if a == 3 or a == 4:
        if b == 3 or b == 4:
            print("Yes")
            return
    if a == 6 or a == 7:
        if b == 6 or b == 7:
            print("Yes")
            return
    if a == 10 or a == 11:
        if b == 10 or b == 11:
            print("Yes")
            return
    print("No")
