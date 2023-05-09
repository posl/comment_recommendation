def main():
    x, y = input().split()
    if x == y:
        print(x)
    else:
        print(3 - int(x) - int(y))
main()
