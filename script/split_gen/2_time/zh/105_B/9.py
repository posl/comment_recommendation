def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0 or N % 11 == 0:
        print("Yes")
    elif N % 15 == 0 or N % 19 == 0 or N % 23 == 0 or N % 27 == 0:
        print("Yes")
    elif N % 31 == 0 or N % 35 == 0 or N % 39 == 0 or N % 43 == 0:
        print("Yes")
    elif N % 47 == 0 or N % 51 == 0 or N % 55 == 0 or N % 59 == 0:
        print("Yes")
    elif N % 63 == 0 or N % 67 == 0 or N % 71 == 0 or N % 75 == 0:
        print("Yes")
    elif N % 79 == 0 or N % 83 == 0 or N % 87 == 0 or N % 91 == 0:
        print("Yes")
    elif N % 95 == 0 or N % 99 == 0:
        print("Yes")
    else:
        print("No")
