def problems113_b():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min = 100000000
    index = 0
    for i in range(n):
        if abs(t - h[i]*0.006 - a) < min:
            min = abs(t - h[i]*0.006 - a)
            index = i
    print(index + 1)

if __name__ == '__main__':
    problems113_b()