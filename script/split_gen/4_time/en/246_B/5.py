def main():
    a, b = map(int, input().split())
    dist = (a**2 + b**2)**0.5
    print(a / dist, b / dist)
