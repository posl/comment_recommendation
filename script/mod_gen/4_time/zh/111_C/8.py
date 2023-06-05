def main():
    n = int(input())
    v = list(map(int, input().split()))
    even = v[0::2]
    odd = v[1::2]
    if len(set(even)) == 1 and len(set(odd)) == 1:
        if even[0] == odd[0]:
            print(n // 2)
        else:
            print(0)
    elif len(set(even)) == 1:
        print(n // 2 - odd.count(even[0]))
    elif len(set(odd)) == 1:
        print(n // 2 - even.count(odd[0]))
    else:
        print(min(n // 2 - even.count(max(set(even), key=even.count)), n // 2 - odd.count(max(set(odd), key=odd.count))))
main()
