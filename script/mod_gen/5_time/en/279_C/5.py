def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    s = ["".join(sorted(x)) for x in s]
    t = ["".join(sorted(x)) for x in t]
    print("Yes" if s == t else "No")

if __name__ == '__main__':
    main()