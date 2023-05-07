def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0 or N % 4 == 2:
        print("Yes")
    else:
        print("No")
