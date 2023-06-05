def main():
    h,w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    t = [list(input()) for _ in range(h)]
    s = [list(x) for x in zip(*s)]
    t = [list(x) for x in zip(*t)]
    s.sort()
    t.sort()
    print("Yes" if s == t else "No")

if __name__ == '__main__':
    main()