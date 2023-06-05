def main():
    a, b = map(int, input().split())
    a = sum(map(int, str(a)))
    b = sum(map(int, str(b)))
    print(a if a > b else b)
