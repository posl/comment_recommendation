def main():
    n = int(input())
    a = set(range(1, 2 * n + 2))
    b = set()
    while True:
        print(min(a - b))
        b.add(int(input()))
        if 0 in b:
            break
        print(min(a - b))
        b.add(int(input()))
        if 0 in b:
            break
main()
