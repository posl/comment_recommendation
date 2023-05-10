def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    v = list(map(int, input().split()))
    odd = [0] * 100005
    even = [0] * 100005
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
        print(min(n - even_max - odd[odd_max], n - odd_max - even[even_max]))
    else:
        if even_max > odd_max:
            even[even_max] = 0
            odd[odd_max] = 0
            print(n - even_max - odd[odd_max])
        else:
            even[even_max] = 0
            odd[odd_max] = 0
            print(n - odd_max - even[even_max])
