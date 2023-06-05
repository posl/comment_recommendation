def replace1with9and9with1(n):
    n1 = n // 100
    n2 = n // 10 % 10
    n3 = n % 10
    n1 = 9 if n1 == 1 else 1
    n2 = 9 if n2 == 1 else 1
    n3 = 9 if n3 == 1 else 1
    return n1 * 100 + n2 * 10 + n3

if __name__ == '__main__':
    replace1with9and9with1()