def problem200_a():
    #解法1
    n = int(input())
    if n % 100 == 0:
        print(n // 100)
    else:
        print(n // 100 + 1)
    #解法2
    #print((n + 99) // 100)

if __name__ == '__main__':
    problem200_a()