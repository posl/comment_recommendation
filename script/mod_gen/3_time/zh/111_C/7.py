def solve():
    n = int(input())
    v = [int(_) for _ in input().split()]
    even = v[::2]
    odd = v[1::2]
    even_count = {}
    odd_count = {}
    for e in even:
        if e in even_count.keys():
            even_count[e] += 1
        else:
            even_count[e] = 1
    for o in odd:
        if o in odd_count.keys():
            odd_count[o] += 1
        else:
            odd_count[o] = 1
    if len(even_count.keys()) == 1 and len(odd_count.keys()) == 1:
        if even_count.keys() == odd_count.keys():
            print(n // 2)
        else:
            print(0)
    elif len(even_count.keys()) == 1 and len(odd_count.keys()) == 2:
        if even_count.keys() == odd_count.keys():
            print(n // 2)
        else:
            print(0)
    elif len(even_count.keys()) == 2 and len(odd_count.keys()) == 1:
        if even_count.keys() == odd_count.keys():
            print(n // 2)
        else:
            print(0)
    else:
        even_max = max(even_count.values())
        odd_max = max(odd_count.values())
        even_max_key = 0
        odd_max_key = 0
        for key, value in even_count.items():
            if value == even_max:
                even_max_key = key
        for key, value in odd_count.items():
            if value == odd_max:
                odd_max_key = key
        if even_max_key == odd_max_key:
            even_max2 = 0
            odd_max2 = 0
            for key, value in even_count.items():
                if key != even_max_key:
                    even_max2 = max(even_max2, value)
            for key, value in odd_count.items():
                if key != odd_max_key:
                    odd_max2 = max(odd_max2, value)
            print(n - even_max - odd_max2)
        else:
            print(n - even_max - odd_max)

if __name__ == '__main__':
    solve()