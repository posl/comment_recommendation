def main():
    a, b = map(int, input().split())
    if a == 1:
        print(0)
    else:
        print((b-1) // (a - 1) + 1)
