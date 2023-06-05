def solve():
    N = int(input())
    data = []
    for i in range(N):
        s, t = input().split()
        data.append((s, int(t)))
    data.sort(key=lambda x: (x[0], -x[1]))
    max_t = 0
    max_i = 0
    for i in range(N):
        if data[i][1] > max_t:
            max_t = data[i][1]
            max_i = i
    print(max_i + 1)
