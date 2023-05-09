def main():
    X, Y = map(int, input().split())
    if abs(X-Y) <= 2:
        print("Yes")
    else:
        print("No")
