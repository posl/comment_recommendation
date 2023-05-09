def pascal(n):
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    else:
        last = pascal(n-1)
        return [1] + [last[i] + last[i+1] for i in range(n-1)] + [1]

if __name__ == '__main__':
    pascal()