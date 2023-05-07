def get_min(n, a):
    if n in a:
        return n
    else:
        for i in a:
            if n % i == 0:
                return i
        for i in a:
            if n % i == 1:
                return i
        for i in a:
            if n % i == 2:
                return i
        for i in a:
            if n % i == 3:
                return i
        for i in a:
            if n % i == 4:
                return i
        for i in a:
            if n % i == 5:
                return i
        for i in a:
            if n % i == 6:
                return i
        for i in a:
            if n % i == 7:
                return i
        for i in a:
            if n % i == 8:
                return i
        for i in a:
            if n % i == 9:
                return i
n, k = map(int, input().split())
a = list(map(int, input().split()))
while True:
    m = get_min(n, a)
    n -= m
    if n == 0:
        print(m)
        break

if __name__ == '__main__':
    get_min()