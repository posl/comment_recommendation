def main():
    n = int(input())
    print(1)
    x = int(input())
    if x == 2:
        print(3)
    else:
        print(2)
    while True:
        x = int(input())
        if x == 2 * n + 1:
            break
        print(x + 1)
main()
