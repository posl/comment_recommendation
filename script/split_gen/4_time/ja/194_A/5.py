def main():
    A, B = map(int, input().split())
    if A+B >= 100:
        print(4)
    elif A+B >= 90:
        print(3)
    elif A+B >= 80:
        print(2)
    else:
        print(1)
