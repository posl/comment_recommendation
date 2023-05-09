def main():
    N = int(input())
    S = [input() for _ in range(N)]
    from collections import Counter
    c = Counter(S)
    max_count = max(c.values())
    for k, v in sorted(c.items()):
        if v == max_count:
            print(k)

if __name__ == '__main__':
    main()