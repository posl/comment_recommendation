def main():
    X, Y = map(int, input().split())
    if X * 4 < Y or Y % 2 == 1:
        print("No")
    else:
        print("Yes")
