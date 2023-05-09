def main():
    from collections import Counter
    n = int(input())
    c = Counter()
    for i in range(n):
        c[input()] += 1
    print(c.most_common()[0][0])

if __name__ == '__main__':
    main()