def main():
    a, b = map(int, input().split())
    if a > 0 and b == 0:
        print("Gold")
    elif a == 0 and b > 0:
        print("Silver")
    elif a > 0 and b > 0:
        print("Alloy")
    else:
        print("error")
