def main():
    n = int(input())
    v = list(map(int, input().split()))
    odd = v[0::2]
    even = v[1::2]
    odd_count = {}
    even_count = {}
    for i in range(n//2):
        if odd[i] not in odd_count:
            odd_count[odd[i]] = 1
        else:
            odd_count[odd[i]] += 1
        if even[i] not in even_count:
            even_count[even[i]] = 1
        else:
            even_count[even[i]] += 1
    odd_count = sorted(odd_count.items(), key=lambda x:x[1], reverse=True)
    even_count = sorted(even_count.items(), key=lambda x:x[1], reverse=True)
    if odd_count[0][0] != even_count[0][0]:
        print(n - odd_count[0][1] - even_count[0][1])
    elif len(odd_count) == 1 and len(even_count) == 1:
        print(n//2)
    elif len(odd_count) == 1:
        print(n//2 - even_count[1][1])
    elif len(even_count) == 1:
        print(n//2 - odd_count[1][1])
    else:
        print(min(n - odd_count[0][1] - even_count[1][1], n - odd_count[1][1] - even_count[0][1]))

if __name__ == '__main__':
    main()