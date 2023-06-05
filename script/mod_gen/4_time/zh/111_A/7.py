def problem111_a():
    n = input()
    n = int(n)
    n1 = n // 100
    n2 = (n % 100) // 10
    n3 = n % 10
    n1 = 9 if n1 == 1 else 1
    n2 = 9 if n2 == 1 else 1
    n3 = 9 if n3 == 1 else 1
    print(n1 * 100 + n2 * 10 + n3)

if __name__ == '__main__':
    problem111_a()