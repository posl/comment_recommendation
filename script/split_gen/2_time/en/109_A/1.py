def main():
    A, B = map(int, input().split())
    if (A == 1 and B == 2) or (A == 2 and B == 1):
        print("No")
    else:
        print("Yes")
