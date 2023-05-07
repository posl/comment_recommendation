def get_max_digit(a, m):
    for i in range(m-1, -1, -1):
        if a[i] <= n:
            return a[i]
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a.reverse()

if __name__ == '__main__':
    get_max_digit()