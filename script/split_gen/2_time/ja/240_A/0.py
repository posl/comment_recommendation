def main():
    a, b = map(int, input().split())
    if a == 1 and b == 10:
        print("Yes")
    elif abs(a - b) == 1:
        print("Yes")
    else:
        print("No")
