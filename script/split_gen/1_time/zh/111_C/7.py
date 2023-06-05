def main():
    n = int(input())
    v = list(map(int, input().split()))
    even = v[0::2]
    odd = v[1::2]
    if len(set(even)) == 1 and len(set(odd)) == 1:
        if even[0] == odd[0]:
            print(len(v) // 2)
        else:
            print(0)
    else:
        if len(set(even)) == 1:
            print(len(v) // 2 - odd.count(even[0]))
        elif len(set(odd)) == 1:
            print(len(v) // 2 - even.count(odd[0]))
        else:
            print(len(v) // 2 - max(odd.count(max(set(odd), key=odd.count)), even.count(max(set(even), key=even.count))))
