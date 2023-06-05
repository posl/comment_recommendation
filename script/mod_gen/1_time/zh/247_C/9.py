def recursion(n):
    if n == 1:
        return [1]
    else:
        return recursion(n-1) + [n] + recursion(n-1)

if __name__ == '__main__':
    recursion()