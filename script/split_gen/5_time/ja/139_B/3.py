def main():
    a, b = map(int, input().split())
    if b == 1:
        print(0)
    else:
        if b % (a-1) == 0:
            print(b // (a-1))
        else:
            print(b // (a-1) + 1)
