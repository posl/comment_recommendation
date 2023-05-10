def main():
    n, t = map(int, input().split())
    min_cost = t
    for i in range(n):
        c, ti = map(int, input().split())
        if ti <= t and c < min_cost:
            min_cost = c
    if min_cost == t:
        print("TLE")
    else:
        print(min_cost)

if __name__ == '__main__':
    main()