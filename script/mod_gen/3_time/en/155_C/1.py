def main():
    N = int(input())
    d = {}
    for i in range(N):
        S = input()
        if S in d:
            d[S] += 1
        else:
            d[S] = 1
    max_count = max(d.values())
    for key, value in sorted(d.items()):
        if value == max_count:
            print(key)

if __name__ == '__main__':
    main()