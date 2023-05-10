def main():
    n = int(input())
    v = list(map(int, input().split()))
    even = [0] * 100001
    odd = [0] * 100001
    for i in range(n):
        if i % 2 == 0:
            even[v[i]] += 1
        else:
            odd[v[i]] += 1
    even_max = 0
    even_max2 = 0
    even_max_index = 0
    even_max2_index = 0
    odd_max = 0
    odd_max2 = 0
    odd_max_index = 0
    odd_max2_index = 0
    for i in range(100001):
        if even_max < even[i]:
            even_max2 = even_max
            even_max2_index = even_max_index
            even_max = even[i]
            even_max_index = i
        elif even_max2 < even[i]:
            even_max2 = even[i]
            even_max2_index = i
        if odd_max < odd[i]:
            odd_max2 = odd_max
            odd_max2_index = odd_max_index
            odd_max = odd[i]
            odd_max_index = i
        elif odd_max2 < odd[i]:
            odd_max2 = odd[i]
            odd_max2_index = i
    if even_max_index != odd_max_index:
        print(n - even_max - odd_max)
    else:
        print(min(n - even_max - odd_max2, n - even_max2 - odd_max))
