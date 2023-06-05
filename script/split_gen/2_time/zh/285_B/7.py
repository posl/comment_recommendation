def main():
    a,b = map(int,input().split())
    if a < b:
        if b - a == 1 or b - a == 4 or b - a == 3:
            print("Yes")
        else:
            print("No")
    else:
        if a - b == 1 or a - b == 4 or a - b == 3:
            print("Yes")
        else:
            print("No")
