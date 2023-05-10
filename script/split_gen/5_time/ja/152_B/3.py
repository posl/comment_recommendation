def main():
    a,b = map(int, input().split())
    if a == b:
        print(str(a) * b)
    elif a < b:
        print(str(a) * b)
    else:
        print(str(b) * a)
