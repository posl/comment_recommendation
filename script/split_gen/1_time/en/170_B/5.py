def main():
    X, Y = map(int, input().split())
    if Y % 2 == 0:
        if X * 4 >= Y and X * 2 <= Y:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
