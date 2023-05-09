def main():
    n, t = map(int, input().split())
    c = []
    for _ in range(n):
        c_i, t_i = map(int, input().split())
        if t_i <= t:
            c.append(c_i)
    if len(c) == 0:
        print("TLE")
    else:
        print(min(c))

if __name__ == '__main__':
    main()