def main():
    n, m, t = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    charge = n
    prev = 0
    for a, b in ab:
        charge -= a - prev
        if charge <= 0:
            print("No")
            return
        charge += b - a
        if charge > n:
            charge = n
        prev = b
    charge -= t - prev
    if charge <= 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()