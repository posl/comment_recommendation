def main():
    a, b = map(int, input().split())
    if a + b > 100:
        print("error")
        return
    if a >= 15 and b >= 8:
        print(1)
    elif a >= 10 and b >= 3:
        print(2)
    elif a >= 3:
        print(3)
    else:
        print(4)