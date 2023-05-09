def problems281_c():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    r = t % s
    for i in range(n):
        if r <= a[i]:
            print(i + 1, r)
            break
        r -= a[i]

if __name__ == '__main__':
    problems281_c()