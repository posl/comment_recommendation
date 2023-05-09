def main():
    a, b = map(int, input().split())
    print("Yes" if a <= b <= a * 6 else "No")
