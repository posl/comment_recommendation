def solve():
    n = int(input())
    v = list(map(int,input().split()))
    even = [0] * 100001
    odd = [0] * 100001
    for i in range(n):
        if i % 2 == 0:
            even[v[i]] += 1
        else:
            odd[v[i]] += 1
    even_max = max(even)
    odd_max = max(odd)
    if even_max == odd_max:
        even[0] = 0
        odd[0] = 0
        even_max2 = max(even)
        odd_max2 = max(odd)
        print(n - max(even_max + odd_max2, even_max2 + odd_max))
    else:
        print(n - even_max - odd_max)

if __name__ == '__main__':
    solve()