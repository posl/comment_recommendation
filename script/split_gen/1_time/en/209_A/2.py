def main():
    a, b = map(int, input().split())
    print(max(0, b - a + 1))
