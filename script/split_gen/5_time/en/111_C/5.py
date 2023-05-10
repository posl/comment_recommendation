def main():
    n = int(input())
    v = list(map(int, input().split()))
    even = v[0::2]
    odd = v[1::2]
    even_count = {}
    odd_count = {}
    for i in range(n//2):
        if even[i] in even_count:
            even_count[even[i]] += 1
        else:
            even_count[even[i]] = 1
        if odd[i] in odd_count:
            odd_count[odd[i]] += 1
        else:
            odd_count[odd[i]] = 1
    even_count = sorted(even_count.items(), key=lambda x: x[1], reverse=True)
    odd_count = sorted(odd_count.items(), key=lambda x: x[1], reverse=True)
    if even_count[0][0] == odd_count[0][0]:
        if len(even_count) == 1 and len(odd_count) == 1:
            print(n//2)
        elif len(even_count) == 1:
            print(n//2 - odd_count[1][1])
        elif len(odd_count) == 1:
            print(n//2 - even_count[1][1])
        else:
            print(min(n//2 - even_count[1][1] - odd_count[0][1], n//2 - even_count[0][1] - odd_count[1][1]))
    else:
        print(n//2 - even_count[0][1] - odd_count[0][1])
