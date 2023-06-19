def main():
    a, b, c, d = map(int, input().split())
    if (a * 60 + b) < (c * 60 + d):
        print("High")
    else:
        print("Low")
