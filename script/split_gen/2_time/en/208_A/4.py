def main():
    A, B = map(int, input().split())
    if A >= 1 and A <= 100 and B >= 1 and B <= 1000:
        if A * 1 <= B <= A * 6:
            print("Yes")
        else:
            print("No")
    else:
        print("Input Error")
