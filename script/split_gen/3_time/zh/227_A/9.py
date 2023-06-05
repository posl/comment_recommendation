def main():
    n, k, a = map(int, input().split())
    print((a + k - 1) % n or n)
