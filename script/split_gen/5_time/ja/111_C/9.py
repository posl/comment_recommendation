def main():
    n = int(input())
    v = list(map(int, input().split()))
    odd = {}
    even = {}
    for i in range(n):
        if i % 2 == 0:
            if v[i] in even:
                even[v[i]] += 1
            else:
                even[v[i]] = 1
        else:
            if v[i] in odd:
                odd[v[i]] += 1
            else:
                odd[v[i]] = 1
    odd = sorted(odd.items(), key=lambda x: x[1], reverse=True)
    even = sorted(even.items(), key=lambda x: x[1], reverse=True)
    if odd[0][0] != even[0][0]:
        print(n - odd[0][1] - even[0][1])
    elif len(odd) == 1 and len(even) == 1:
        print(n // 2)
    elif len(odd) == 1:
        print(n - even[1][1])
    elif len(even) == 1:
        print(n - odd[1][1])
    else:
        print(min(n - odd[0][1] - even[1][1], n - odd[1][1] - even[0][1]))
