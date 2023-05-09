def main():
    a, b = map(int, input().split())
    if a * b > 0:
        if str(a) * b < str(b) * a:
            print(str(a) * b)
        else:
            print(str(b) * a)
