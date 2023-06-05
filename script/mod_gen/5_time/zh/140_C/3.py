def max_sum(n, b):
    a = [b[0]]
    for i in range(1, n-1):
        a.append(max(b[i], b[i-1]))
    a.append(b[n-2])
    return sum(a)

if __name__ == '__main__':
    max_sum()