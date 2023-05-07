def main():
    N = int(input())
    V = list(map(int, input().split()))
    if N == 2:
        print(0)
        return
    even = V[::2]
    odd = V[1::2]
    even_c = Counter(even)
    odd_c = Counter(odd)
    even_max = even_c.most_common()[0]
    odd_max = odd_c.most_common()[0]
    if even_max[0] == odd_max[0]:
        if len(even_c) == 1:
            even_max = even_c.most_common()[1]
        elif len(odd_c) == 1:
            odd_max = odd_c.most_common()[1]
        else:
            even_max = even_c.most_common()[1]
            odd_max = odd_c.most_common()[1]
    print(N - even_max[1] - odd_max[1])

if __name__ == '__main__':
    main()