def main():
    a, b = map(int, input().split())
    if a+b >= 100:
        print(1)
    elif a+b >= 50:
        print(2)
    elif a+b >= 3:
        print(3)
    else:
        print(4)
