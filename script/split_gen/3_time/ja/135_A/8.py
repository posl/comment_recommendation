def main():
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    if (b - a) % 2:
        print("IMPOSSIBLE")
    else:
        print((a + b) // 2)
