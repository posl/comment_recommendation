def main():
    x, y, n = map(int, input().split())
    print((n//3)*min(x*3,y) + (n%3)*x)
