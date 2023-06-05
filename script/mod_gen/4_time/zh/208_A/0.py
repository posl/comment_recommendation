def f(n, m):
    if n > m:
        return "No"
    elif n == m:
        return "Yes"
    else:
        return f(n+6, m)

if __name__ == '__main__':
    f()