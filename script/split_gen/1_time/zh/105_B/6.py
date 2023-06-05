def main():
    N = int(input())
    if N % 4 == 0:
        print("Yes")
    elif N % 7 == 0:
        print("Yes")
    elif N % 11 == 0:
        print("Yes")
    elif N % 4 + N % 7 == 11:
        print("Yes")
    elif N % 4 + N % 11 == 7:
        print("Yes")
    elif N % 7 + N % 11 == 4:
        print("Yes")
    elif N % 4 + N % 7 + N % 11 == 0:
        print("Yes")
    else:
        print("No")
