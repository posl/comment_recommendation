def problems256_b():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        p += a[i]
        if p >= 4:
            print(i + 1)
            return
    print(-1)

if __name__ == '__main__':
    problems256_b()