def main():
    # input
    A, B, C = map(int, input().split())
    # output
    if (A**2 + B**2 < C**2):
        print("Yes")
    else:
        print("No")
