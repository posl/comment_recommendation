def main():
    d,n = map(int,input().split())
    if d == 0:
        print(n if n != 100 else 101)
    elif d == 1:
        print(n * 100 if n != 100 else 10100)
    else:
        print(n * 10000 if n != 100 else 1010000)
