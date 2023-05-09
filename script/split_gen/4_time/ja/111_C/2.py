def main():
    n = int(input())
    v = list(map(int, input().split()))
    odd = []
    even = []
    for i in range(n):
        if i%2 == 0:
            even.append(v[i])
        else:
            odd.append(v[i])
    even_count = []
    odd_count = []
    for i in range(1, max(v)+1):
        even_count.append(even.count(i))
        odd_count.append(odd.count(i))
    even_max = max(even_count)
    odd_max = max(odd_count)
    if even_count.index(even_max) == odd_count.index(odd_max):
        if even_max == odd_max:
            even_count[even_count.index(even_max)] = 0
            odd_count[odd_count.index(odd_max)] = 0
            even_max = max(even_count)
            odd_max = max(odd_count)
        else:
            even_count[even_count.index(even_max)] = 0
            even_max = max(even_count)
            odd_count[odd_count.index(odd_max)] = 0
            odd_max = max(odd_count)
    even_sum = len(even) - even_max
    odd_sum = len(odd) - odd_max
    print(even_sum + odd_sum)
