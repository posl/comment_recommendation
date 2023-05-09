def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1 or (a == 2 and b == 2):
        print("No")
    else:
        print("Yes")
