def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1 or (a == 9 and b == 10) or (a == 10 and b == 9):
        print("Yes")
    else:
        print("No")
