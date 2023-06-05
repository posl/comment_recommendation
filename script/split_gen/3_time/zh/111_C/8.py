def main():
    n = int(input())
    v = list(map(int, input().split()))
    even = v[::2]
    odd = v[1::2]
    if len(set(even)) == 1 and len(set(odd)) == 1:
        if even[0] == odd[0]:
            print(len(even))
        else:
            print(0)
    elif len(set(even)) == 1:
        print(len(odd) - odd.count(even[0]))
    elif len(set(odd)) == 1:
        print(len(even) - even.count(odd[0]))
    else:
        print(min(len(odd) - odd.count(even[0]), len(even) - even.count(odd[0])))
