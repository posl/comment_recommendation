def main():
    h, m = map(int, input().split())
    if m == 0:
        if h == 0:
            print("0 0")
        else:
            print(h, 0)
    else:
        print(h, m)
