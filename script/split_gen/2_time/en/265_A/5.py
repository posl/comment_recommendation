def main():
    x, y, n = map(int, input().split())
    print(min((n//3)*y + (n%3)*x, (n//3+1)*y))
