def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1 or abs(a - b) == 1:
        print("Yes")
    else:
        print("No")
