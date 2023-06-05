def main():
    n = int(input())
    v = list(map(int, input().split()))
    odd = v[0::2]
    even = v[1::2]
    odd_count = {}
    even_count = {}
    for i in range(n//2):
        if odd[i] in odd_count:
            odd_count[odd[i]] += 1
        else:
            odd_count[odd[i]] = 1
        if even[i] in even_count:
            even_count[even[i]] += 1
        else:
            even_count[even[i]] = 1
    odd_max = max(odd_count.values())
    even_max = max(even_count.values())
    if odd_max == even_max:
        if len(odd_count) == 1 and len(even_count) == 1:
            print(n//2)
        else:
            print(n - odd_max - even_max)
    elif odd_max > even_max:
        if len(even_count) == 1:
            print(n - odd_max)
        else:
            print(n - odd_max - even_max)
    else:
        if len(odd_count) == 1:
            print(n - even_max)
        else:
            print(n - odd_max - even_max)
