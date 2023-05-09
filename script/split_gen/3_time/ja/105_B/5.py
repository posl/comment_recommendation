def main():
    n = int(input())
    if n%4 == 0 or n%7 == 0 or n%4 == 7 or n%7 == 4:
        print("Yes")
    else:
        print("No")
