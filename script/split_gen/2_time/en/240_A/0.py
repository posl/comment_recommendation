def main():
    a, b = map(int, input().split())
    if abs(a - b) == 1:
        print("Yes")
    else:
        print("No")
