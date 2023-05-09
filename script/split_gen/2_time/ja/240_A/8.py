def main():
    a, b = map(int, input().split())
    if a < 4 and b < 4:
        print("Yes")
    elif a > 3 and b > 3:
        print("Yes")
    else:
        print("No")
