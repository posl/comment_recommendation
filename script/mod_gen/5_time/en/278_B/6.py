def confusing_time(h,m):
    while True:
        m += 1
        if m == 60:
            h += 1
            m = 0
            if h == 24:
                h = 0
        if h // 10 == m % 10 and h % 10 == m // 10:
            return h, m
h, m = map(int, input().split())
print(*confusing_time(h, m))

if __name__ == '__main__':
    confusing_time()