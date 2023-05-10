def solve():
    h = [int(i) for i in input().split()]
    w = [int(i) for i in input().split()]
    def is_valid(h, w):
        if sum(h) != sum(w):
            return False
        for i in range(3):
            if h[i] + h[(i + 1) % 3] < w[i] + w[(i + 1) % 3]:
                return False
        return True
    def f(n):
        return 1 if n == 0 else n * f(n - 1)
    if is_valid(h, w):
        print(f(sum(h)) // f(h[0]) // f(h[1]) // f(h[2]))
    else:
        print(0)
solve()

if __name__ == '__main__':
    solve()