def abc258_a():
    k = int(input())
    print(21 + (k + 9) // 60, (k + 9) % 60, sep=':')

if __name__ == '__main__':
    abc258_a()