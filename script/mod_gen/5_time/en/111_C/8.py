def main():
    N = int(input())
    V = list(map(int, input().split()))
    even = V[0::2]
    odd = V[1::2]
    even_count = {}
    odd_count = {}
    for e in even:
        if e in even_count:
            even_count[e] += 1
        else:
            even_count[e] = 1
    for o in odd:
        if o in odd_count:
            odd_count[o] += 1
        else:
            odd_count[o] = 1
    even_count = sorted(even_count.items(), key=lambda x:x[1], reverse=True)
    odd_count = sorted(odd_count.items(), key=lambda x:x[1], reverse=True)
    # print(even_count)
    # print(odd_count)
    if even_count[0][0] != odd_count[0][0]:
        print(N - even_count[0][1] - odd_count[0][1])
    elif len(even_count) == 1 and len(odd_count) == 1:
        print(N//2)
    elif len(even_count) == 1:
        print(N//2 - odd_count[1][1])
    elif len(odd_count) == 1:
        print(N//2 - even_count[1][1])
    else:
        print(min(N - even_count[0][1] - odd_count[1][1], N - even_count[1][1] - odd_count[0][1]))

if __name__ == '__main__':
    main()