def main():
    a, b = map(int, input().split())
    if a == b:
        print(str(a)*a)
    elif a > b:
        print(str(b)*b)
    else:
        print(str(a)*a)
