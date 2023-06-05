def solve(n, v):
    even = v[0::2]
    odd = v[1::2]
    even_count = 0
    odd_count = 0
    even_max = 0
    odd_max = 0
    for i in range(1, 10**5+1):
        if even.count(i) > even_count:
            even_count = even.count(i)
            even_max = i
        if odd.count(i) > odd_count:
            odd_count = odd.count(i)
            odd_max = i
    if even_max != odd_max:
        return n - even_count - odd_count
    else:
        even_count2 = 0
        odd_count2 = 0
        even_max2 = 0
        odd_max2 = 0
        for i in range(1, 10**5+1):
            if even.count(i) > even_count2 and i != even_max:
                even_count2 = even.count(i)
                even_max2 = i
            if odd.count(i) > odd_count2 and i != odd_max:
                odd_count2 = odd.count(i)
                odd_max2 = i
        if even_count2 > odd_count2:
            return n - even_count - odd_count2
        else:
            return n - even_count2 - odd_count
n = int(input())
v = list(map(int, input().split()))
print(solve(n, v))
