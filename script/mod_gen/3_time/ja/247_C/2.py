def make_s(n):
    if n == 1:
        return [1]
    else:
        return make_s(n-1) + [n] + make_s(n-1)
n = int(input())
print(" ".join(map(str,make_s(n))))

if __name__ == '__main__':
    make_s()