def func():
    N = int(input())
    p = list(map(int, input().split()))
    p.insert(0, 0)
    max_num = 0
    for i in range(1, N+1):
        num = 1
        j = p[i]
        while j != -1:
            num += 1
            j = p[j]
        max_num = max(max_num, num)
    print(max_num)
func()
