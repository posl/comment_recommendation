def divisor(n):
    div = []
    for i in range(1, n + 1):
        if n % i == 0:
            div.append(i)
    return div

if __name__ == '__main__':
    divisor()