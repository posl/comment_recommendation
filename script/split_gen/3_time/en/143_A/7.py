def main():
    A, B = map(int, input().split())
    print((A - B) if (A - B) > 0 else 0)
