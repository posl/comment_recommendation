def main():
    n = int(input())
    v = list(map(int, input().split()))
    odd = v[0::2]
    even = v[1::2]
    odd_count = {}
    even_count = {}
    for i in odd:
        if i in odd_count:
            odd_count[i] += 1
        else:
            odd_count[i] = 1
    for i in even:
        if i in even_count:
            even_count[i] += 1
        else:
            even_count[i] = 1
    odd_count_sorted = sorted(odd_count.items(), key=lambda x: x[1], reverse=True)
    even_count_sorted = sorted(even_count.items(), key=lambda x: x[1], reverse=True)
    if odd_count_sorted[0][0] != even_count_sorted[0][0]:
        print(n - odd_count_sorted[0][1] - even_count_sorted[0][1])
    else:
        if len(odd_count_sorted) == 1 and len(even_count_sorted) == 1:
            print(n // 2)
        elif len(odd_count_sorted) == 1:
            print(n - even_count_sorted[0][1])
        elif len(even_count_sorted) == 1:
            print(n - odd_count_sorted[0][1])
        else:
            if odd_count_sorted[1][1] > even_count_sorted[1][1]:
                print(n - odd_count_sorted[1][1] - even_count_sorted[0][1])
            else:
                print(n - odd_count_sorted[0][1] - even_count_sorted[1][1])
