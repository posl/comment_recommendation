def main():
    a, b = map(int, input().split())
    if 6*a >= b >= a:
        print("Yes")
    else:
        print("No")
