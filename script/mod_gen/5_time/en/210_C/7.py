def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    from collections import Counter
    counter = Counter(c[:k])
    max_count = len(counter)
    for i in range(k, n):
        counter[c[i]] += 1
        counter[c[i-k]] -= 1
        if counter[c[i-k]] == 0:
            del counter[c[i-k]]
        max_count = max(max_count, len(counter))
    print(max_count)

if __name__ == '__main__':
    main()