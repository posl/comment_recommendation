def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print((n + min(a, b, c, d, e) - 1) // min(a, b, c, d, e) + 4)
