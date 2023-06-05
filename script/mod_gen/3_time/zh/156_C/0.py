def func(l):
    l.sort()
    n = len(l)
    if n % 2 == 1:
        return sum([(l[i] - l[n/2]) ** 2 for i in range(n)])
    else:
        return min(sum([(l[i] - l[n/2]) ** 2 for i in range(n)]), sum([(l[i] - l[n/2 - 1]) ** 2 for i in range(n)]))

if __name__ == '__main__':
    func()