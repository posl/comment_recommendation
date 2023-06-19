def main():
    a,b = map(int,input().split())
    if (a > 15 or a < 1) or (b > 15 or b < 1):
        print("No")
    elif (b - a == 1) or (b - a == 4):
        print("Yes")
    else:
        print("No")
