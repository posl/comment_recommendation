def problems124_b():
    n = int(input())
    h = list(map(int,input().split()))
    max_h = 0
    count = 0
    for i in range(n):
        if max_h <= h[i]:
            max_h = h[i]
            count += 1
    print(count)

if __name__ == '__main__':
    problems124_b()