def main():
    a, b = map(int, input().split())
    if a <= b and b <= 6*a:
        print("Yes")
    else:
        print("No")
