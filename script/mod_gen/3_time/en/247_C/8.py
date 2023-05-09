def make_seq(n):
    if n == 1:
        return [1]
    else:
        return make_seq(n-1) + [n] + make_seq(n-1)
N = int(input())
print(*make_seq(N))

if __name__ == '__main__':
    make_seq()