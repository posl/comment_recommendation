def main():
    a, b = map(int, input().split())
    print("Easy" if a + b < 10 ** 19 else "Hard")
