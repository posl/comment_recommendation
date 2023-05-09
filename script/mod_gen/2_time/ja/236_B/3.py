def main():
    from collections import Counter
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    for i in c:
        if c[i] == 1:
            print(i)
            break

if __name__ == '__main__':
    main()