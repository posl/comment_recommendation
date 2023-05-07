def to_n_ary(n, ary):
    if n == 0:
        return ary
    if n % (-2) == 0:
        ary.append("0")
        return to_n_ary(n // (-2), ary)
    else:
        ary.append("1")
        return to_n_ary((n - 1) // (-2), ary)
n = int(input())

if __name__ == '__main__':
    to_n_ary()