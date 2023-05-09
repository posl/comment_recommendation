def main():
    a, b = map(int, input().split())
    print(b-a+1 if b-a+1 > 0 else 0)
