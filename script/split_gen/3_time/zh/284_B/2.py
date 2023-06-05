def problems284_b():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        count = 0
        for i in range(n):
            if a[i] % 2 == 1:
                count += 1
        print(count)
