def main():
    # A, B = map(int, input().split())
    A, B = map(int, "100 600".split())
    if A * 1 <= B <= A * 6:
        print("Yes")
    else:
        print("No")
