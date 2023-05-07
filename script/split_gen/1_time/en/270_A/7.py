def main():
    a, b = map(int, input().split())
    print(a + b + max(0, a+b-6))
