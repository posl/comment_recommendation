def main():
    x, y = map(int, input().split())
    if (y % 2 == 0) and (y / 2 <= x) and (y / 2 >= x - 2):
        print("Yes")
    else:
        print("No")
