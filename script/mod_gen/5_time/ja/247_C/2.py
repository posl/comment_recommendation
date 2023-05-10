def make_s(n):
    if n == 1:
        return [1]
    else:
        s = make_s(n-1)
        return s + [n] + s
N = int(input())
print(*make_s(N))

if __name__ == '__main__':
    make_s()