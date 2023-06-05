def main():
    n = int(input())
    v = list(map(int, input().split()))
    odd = [0] * 100001
    even = [0] * 100001
    for i in range(n):
        if i % 2 == 0:
            even[v[i]] += 1
        else:
            odd[v[i]] += 1
    even_max = max(even)
    odd_max = max(odd)
    if even_max == odd_max:
        even[even_max] = 0
        odd[odd_max] = 0
        print(n - max(max(even), max(odd)))
    else:
        print(n - even_max - odd_max)
