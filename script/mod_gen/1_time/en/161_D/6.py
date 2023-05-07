def lunlun(n):
    if n < 10:
        return n
    elif n < 100:
        return (n % 10) + 10 * lunlun(n // 10)
    else:
        return (n % 10) + 10 * lunlun(n // 10) + 100 * lunlun(n // 100)
K = int(input())
print(lunlun(K))

if __name__ == '__main__':
    lunlun()