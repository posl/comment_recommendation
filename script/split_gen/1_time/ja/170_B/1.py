def main():
    x, y = map(int, input().split())
    if (x*4 >= y) and (x*2 <= y) and (y%2 == 0):
        print("Yes")
    else:
        print("No")
