def main():
    N = int(input())
    if N < -2**31 or N > 2**31 - 1:
        print("No")
    else:
        print("Yes")
