def main():
    x,y = map(int, input().split())
    if x < y and y - x < 3:
        print("Yes")
    elif x > y and x - y < 4:
        print("Yes")
    else:
        print("No")
