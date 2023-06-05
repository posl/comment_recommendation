def problem105_b():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0 or N % 11 == 0:
        print("Yes")
    elif N % 4 == 1 or N % 7 == 1 or N % 11 == 1:
        print("No")
    else:
        print("Yes")
