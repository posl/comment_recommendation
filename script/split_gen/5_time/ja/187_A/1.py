def main():
    a,b = map(int, input().split())
    a = sum(map(int, list(str(a))))
    b = sum(map(int, list(str(b))))
    print(a if a > b else b)
