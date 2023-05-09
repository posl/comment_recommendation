def main():
    s = input()
    q = int(input())
    for _ in range(q):
        t, k = map(int, input().split())
        if t % 3 == 0:
            print(s[(k - 1) % len(s)])
        elif t % 3 == 1:
            if k <= s.count("B"):
                print("B")
            elif k <= s.count("B") + s.count("C"):
                print("C")
            else:
                print("A")
        else:
            if k <= s.count("A"):
                print("A")
            elif k <= s.count("A") + s.count("B"):
                print("B")
            else:
                print("C")

if __name__ == '__main__':
    main()