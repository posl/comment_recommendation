def main():
    a, b = map(int, input().split())
    print("Yes" if a <= b <= 6*a else "No")
