def main():
    A, B = map(int, input().split())
    if A <= 5:
        print("0")
    elif A >= 6 and A <= 12:
        print(B // 2)
    else:
        print(B)
