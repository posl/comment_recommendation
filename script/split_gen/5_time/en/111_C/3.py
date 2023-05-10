def main():
    n = int(input())
    v = list(map(int, input().split()))
    even = {}
    odd = {}
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
    even = sorted(even.items(), key=lambda x:x[1], reverse=True)
    odd = sorted(odd.items(), key=lambda x:x[1], reverse=True)
    if even[0][0] != odd[0][0]:
        print(n - even[0][1] - odd[0][1])
    else:
        if len(even) == 1 and len(odd) == 1:
            print(n // 2)
        elif len(even) == 1:
            print(n - odd[1][1])
        elif len(odd) == 1:
            print(n - even[1][1])
        else:
            print(min(n - even[1][1] - odd[0][1], n - even[0][1] - odd[1][1]))
