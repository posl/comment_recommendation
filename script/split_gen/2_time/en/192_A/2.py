def main():
    x = int(input())
    print(100 - x % 100 if x % 100 != 0 else 0)
