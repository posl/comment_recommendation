def main():
    a, b = (int(x) for x in input().split())
    c, d = (int(x) for x in input().split())
    print(a*d-c*b)
