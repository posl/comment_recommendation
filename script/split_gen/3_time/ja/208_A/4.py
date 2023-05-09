def main():
    A, B = map(int, input().split())
    if 6 * A >= B and A <= B:
        print("Yes")
    else:
        print("No")
