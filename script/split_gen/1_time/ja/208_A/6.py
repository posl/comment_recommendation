def main():
    A, B = map(int, input().split())
    if A * 6 < B:
        print("No")
    elif 1 * A > B:
        print("No")
    else:
        print("Yes")
