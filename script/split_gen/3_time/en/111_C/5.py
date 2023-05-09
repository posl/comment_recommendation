def main():
    n = int(input())
    v = list(map(int, input().split()))
    even = v[::2]
    odd = v[1::2]
    even_c = Counter(even)
    odd_c = Counter(odd)
    even_max = even_c.most_common()[0]
    odd_max = odd_c.most_common()[0]
    if even_max[0] == odd_max[0]:
        if len(even_c) == 1 or len(odd_c) == 1:
            print(n // 2)
        else:
            even_max2 = even_c.most_common()[1]
            odd_max2 = odd_c.most_common()[1]
            print(min(n - even_max[1] - odd_max2[1], n - even_max2[1] - odd_max[1]))
    else:
        print(n - even_max[1] - odd_max[1])
