def odd_number_count():
    n = int(input())
    a = list(map(int, input().split()))
    odd_count = 0
    for i in range(n):
        if a[i] % 2 == 1:
            odd_count += 1
    print(odd_count)
