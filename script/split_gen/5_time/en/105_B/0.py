def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0 or N % 11 == 0 or N % 15 == 0 or N % 18 == 0 or N % 22 == 0 or N % 26 == 0 or N % 30 == 0 or N % 33 == 0 or N % 37 == 0 or N % 40 == 0:
        print("Yes")
    else:
        print("No")
main()
