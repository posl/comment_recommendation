def main():
    n, t = map(int, input().split())
    c = []
    for i in range(n):
        ci, ti = map(int, input().split())
        if ti <= t:
            c.append(ci)
    if len(c) == 0:
        print("TLE")
    else:
        print(min(c))

if __name__ == '__main__':
    main()