def main():
    n = int(input())
    v = list(map(int, input().split()))
    odd = []
    even = []
    for i in range(n):
        if i % 2 == 0:
            even.append(v[i])
        else:
            odd.append(v[i])
    odd.sort()
    even.sort()
    odd.append(-1)
    even.append(-1)
    odd_1 = odd[0]
    even_1 = even[0]
    odd_2 = odd[1]
    even_2 = even[1]
    odd_count = 1
    even_count = 1
    for i in range(1, n):
        if odd[i] == odd_1:
            odd_count += 1
        else:
            odd_2 = odd[i]
            break
    for i in range(1, n):
        if even[i] == even_1:
            even_count += 1
        else:
            even_2 = even[i]
            break
    if odd_1 == even_1:
        if odd_count + even_count < n:
            print(n - odd_count - even_count)
        else:
            print(n - max(odd_count, even_count))
    else:
        print(n - odd_count - even_count)
