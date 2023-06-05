def main():
    base = int(input())
    a, b = map(str, input().split())
    a = int(a, base)
    b = int(b, base)
    print(a*b)
