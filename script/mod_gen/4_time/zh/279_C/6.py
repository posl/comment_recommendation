def main():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    s = ["".join(x) for x in zip(*s)]
    t = ["".join(x) for x in zip(*t)]
    s.sort()
    t.sort()
    if s == t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()