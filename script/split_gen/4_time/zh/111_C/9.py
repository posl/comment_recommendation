def solve():
    n = int(input())
    v = list(map(int, input().split()))
    even = v[::2]
    odd = v[1::2]
    if len(set(even)) == 1 and len(set(odd)) == 1:
        if even[0] == odd[0]:
            print(n // 2)
        else:
            print(0)
    elif len(set(even)) == 1:
        print(n // 2)
    elif len(set(odd)) == 1:
        print(n // 2)
    else:
        print(min(even.count(odd[0]) + odd.count(even[0]), even.count(odd[1]) + odd.count(even[1])))
