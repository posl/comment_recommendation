def main():
    a, b = map(int, input().split())
    if (a <= 8 and b <= 8) or (a > 8 and b > 8):
        print("Yes")
    else:
        print("No")
